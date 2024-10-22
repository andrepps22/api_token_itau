from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    id: int
    username: str
    nome: str
    email: EmailStr
    senha: str

    
    