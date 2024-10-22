from pydantic_settings import BaseSettings
from typing import ClassVar
from sqlalchemy.orm import registry
import os


class Setting(BaseSettings):
    DB_URL: str = 'sqlite+aiosqlite:///sqldblite.db'
    DBBaseModel: ClassVar = registry()
    API_VERSION: str = '/api/v2'
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 1 semana
    
    class Config:
        case_sensitive = True
        env_file = '.env'
        
        
setting = Setting()