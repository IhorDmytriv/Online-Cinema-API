from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import get_settings

settings = get_settings()

DATABASE_URL = f"sqlite+aiosqlite:///{settings.PATH_TO_DB}"

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSQLiteSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide an asynchronous database session.

    This function returns an async generator yielding a new database session.
    It ensures that the session is properly closed after use.

    :return: An asynchronous generator yielding an AsyncSession instance.
    """
    async with AsyncSQLiteSessionLocal() as session:
        yield session
