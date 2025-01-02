from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String, Text
from typing import Optional

# Create async engine
DATABASE_URL = "sqlite+aiosqlite:///./representatives.db"
engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Representative model
class RepresentativeDB(Base):
    __tablename__ = "representatives"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    designation = Column(String)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    city = Column(String, index=True)
    verified = Column(Integer, default=0)  # 0: AI-generated, 1: Verified

# Initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Get database session
async def get_db():
    async with async_session() as session:
        yield session
