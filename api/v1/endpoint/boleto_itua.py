import urllib.parse
from fastapi import APIRouter,status, HTTPException, Request, Depends
from schemas.boleto_itau_shcema import BoletoSchema
from core.buscar_token import buscar_token
from core.config import setting
from core.security import get_current_user
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers=[
        logging.FileHandler("logs/app.log"), logging.StreamHandler()])

router = APIRouter(prefix='/itau/boleto', tags=['boleto'])

logger = logging.getLogger("Boleto")

@router.post('/', status_code=status.HTTP_201_CREATED, description='Realiza o registro dos boletos no Itaú', summary='Registro de boletos do Itaú')
async def post_token(model:BoletoSchema, request:Request, current_user = Depends(get_current_user) ):
    
    logger.info(f"Requisição recebida ip {request.client} no endpoint: {request.url}")    
    crt = urllib.parse.unquote(model.crt)
    key = urllib.parse.unquote(model.key)
    header = [model.Authorization, model.ContentType, model.xitauapikey, model.xitauflowID, model.xitaucorrelationID]
    dados = model.dados
    tipo_chamada = 'Boleto'

    return buscar_token(crt, key, tipo_chamada, header=header, dados=dados)

  
        
    
    