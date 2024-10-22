from core.database import Session
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        try:
            yield session
        finally:
            await session.close()
    