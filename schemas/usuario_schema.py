from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    username: str
    nome: str
    email: EmailStr
    senha: str


class UsuarioPubSchema(UsuarioSchema):
    id: int = None
    username: str
    nome: str
    email: EmailStr
    
    