from jwt import decode, encode
from jwt.exceptions import ExpiredSignatureError, PyJWTError
from pwdlib import PasswordHash
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from core.config import setting
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.deps import get_session
from models.usuario_model import UsuarioModel


pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{setting.API_VERSION}/auth/token')


async def get_password_hash(senha) -> str:
    return pwd_context.hash(senha)
    


async def verify_password(senha, hash_senha) -> bool:
    return pwd_context.verify(senha, hash_senha)


async def get_token(dados:dict):
    to_encode = dados.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=setting.ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    
    encode_jwt = encode(to_encode, setting.JWT_SECRET, algorithm=setting.ALGORITHM)
    return encode_jwt

async def get_current_user(
        db: AsyncSession = Depends(get_session),
        token: str = Depends(oauth2_scheme)
):
    
    credentials_exception = HTTPException(  
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Não foi possivel validar as credenciais',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    payload = decode(token, setting.JWT_SECRET, setting.ALGORITHM)

    username = payload.get('sub')

    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.username == username)
        user = await session.execute(query)
        try:
            if not user:
                raise credentials_exception
        except ExpiredSignatureError:
            raise HTTPException(  
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Token invalido')
        except PyJWTError:
            raise credentials_exception