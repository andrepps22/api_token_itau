import urllib.parse
from fastapi import APIRouter,status, HTTPException, Depends, Request
from schemas.buscar_token_itau_schema import TokenSchemas
from schemas.token_itau_retorno_schema import RetornoTokenSchema
from core.security import get_current_user
from core.buscar_token import buscar_token
from core.config import setting

import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers=[
        logging.FileHandler("logs/app.log"), logging.StreamHandler()])


router = APIRouter(prefix='/itau/token', tags=['Token'])


logger = logging.getLogger("Token")

@router.post('/', response_model=RetornoTokenSchema, status_code=status.HTTP_201_CREATED, description='Realiza um post na api do Itaú e retorna o token', summary='Cria o token')
async def post_token(model:TokenSchemas, request:Request, current_user = Depends(get_current_user)):
    logger.info(f"Requisição recebida ip {request.client} no endpoint: {request.url}")
    crt = urllib.parse.unquote(model.crt)
    key = urllib.parse.unquote(model.key)
    client_id = model.client_id
    secret_key = model.secret_key
    tipo_chamada = 'Token'
    retorno = buscar_token(client_id=client_id, secret_key=secret_key, crt=crt, key=key, tipo_chamada=tipo_chamada)
    return retorno
    
        

        
    
    
    