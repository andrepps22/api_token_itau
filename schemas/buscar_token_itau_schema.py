from pydantic import BaseModel
from typing import Any




class TokenSchemas(BaseModel):
    client_id:str
    secret_key:str
    crt: str
    key: str