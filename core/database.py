from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from core.config import setting

engine: AsyncEngine = create_async_engine(setting.DB_URL)

Session: AsyncSession = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    class_= AsyncSession
)