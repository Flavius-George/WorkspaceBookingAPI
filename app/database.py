from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
USER="postgres"
PASSWORD="password"
PORT="5432"
DB="WSB"
DB_URL=f"postgresql+asyncpg://{USER}:{PASSWORD}@db:{PORT}/{DB}"

engine = create_async_engine(DB_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


