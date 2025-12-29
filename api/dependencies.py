from sqlalchemy.ext.asyncio import async_session

from database import SessionLocal

from dotenv import load_dotenv

load_dotenv()


async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
