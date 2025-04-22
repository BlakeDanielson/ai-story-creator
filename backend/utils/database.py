"""Database utilities for connecting to and working with the database."""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.config import settings

# Create engine based on settings
engine = create_async_engine(
    settings.database_url or "sqlite+aiosqlite:///:memory:",
    echo=settings.db_echo,
    pool_size=settings.db_pool_size,
    max_overflow=settings.db_max_overflow,
)

# Create session factory
async_session_maker = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for database session.
    
    Yields:
        AsyncSession: Database session
        
    Example:
        ```python
        @router.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            # Use db session here
            pass
        ```
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def create_database_tables() -> None:
    """Create all database tables if they don't exist.
    
    This is used for testing and development. In production, 
    use Alembic migrations instead.
    """
    from backend.models.base import Base
    
    async with engine.begin() as conn:
        # Import all models to ensure they're registered with metadata
        # This is a circular import but only used during app startup
        # pylint: disable=import-outside-toplevel, unused-import
        from backend.models import base  # noqa
        
        await conn.run_sync(Base.metadata.create_all)