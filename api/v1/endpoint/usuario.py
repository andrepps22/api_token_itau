from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core.deps import get_session
from core.security import get_password_hash, get_current_user
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchema, UsuarioPubSchema
import logging


router = APIRouter()


@router.post('/usuarios', response_model=UsuarioSchema, status_code=status.HTTP_201_CREATED)
async def post_usuario(usuario: UsuarioSchema, db: AsyncSession = Depends(get_session), current_user = Depends(get_current_user)):
    async with db as session:
        query = insert(UsuarioModel).values(
            username=usuario.username,
            nome=usuario.nome,
            email=usuario.email,
            senha=await get_password_hash(usuario.senha)
        )

        await session.execute(query)
        await session.commit()

    return usuario


@router.get('/usuarios', response_model=List[UsuarioPubSchema], status_code=status.HTTP_200_OK)
async def get_usuarios(db: AsyncSession = Depends(get_session), current_user = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List = result.scalars().all()
        if usuarios:
            return usuarios
