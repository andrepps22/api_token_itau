from sqlalchemy.orm import mapped_column, Mapped
from core.config import setting

reg = setting.DBBaseModel

@reg.mapped_as_dataclass()
class UsuarioModel:
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True)
    nome: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column()
    
    
    __table_args__ = {'extend_existing': True}
    

        