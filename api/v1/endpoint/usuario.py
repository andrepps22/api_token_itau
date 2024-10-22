from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from core.security import get_password_hash, get_current_user
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchema
import logging


router = APIRouter()


@router.post('/usuarios', response_model=UsuarioSchema)
async def post_usuario(usuario: UsuarioSchema, db: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)):
    async with db as session:
        query = insert(UsuarioModel).values(
            id=usuario.id,
            username=usuario.username,
            nome=usuario.nome,
            email=usuario.email,
            senha=await get_password_hash(usuario.senha)
        )

        await session.execute(query)
        await session.commit()

    return usuario
