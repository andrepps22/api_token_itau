from core.config import setting
from fastapi import APIRouter
from api.v1.endpoint import usuario, auth, token_itau, boleto_itua

router = APIRouter(prefix=setting.API_VERSION)


router.include_router(usuario.router)
router.include_router(auth.router)
router.include_router(token_itau.router)
router.include_router(boleto_itua.router)