from fastapi import APIRouter, Depends, HTTPException, status
from core.config import setting
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from core.security import get_token, verify_password
from models.usuario_model import UsuarioModel
from schemas.token_schemas import TokenSchemas

router = APIRouter(prefix='/auth/token', tags=['Auth'])


@router.post('', response_model=TokenSchemas)
async def login_para_acess_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session)):

    async with db as session:
        user = await session.scalar(select(UsuarioModel).where(UsuarioModel.username == form_data.username))

        if not user or not await verify_password(form_data.password, user.senha):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail='Username ou senha incorretas')
    
    access_token = await get_token({'sub': user.username})

    return {'access_token': access_token, 'token_type':'Bearer', 'expire': (setting.ACESS_TOKEN_EXPIRE_MINUTES * 60) }
        