import asyncio
from app.database import engine, Base
from app.models.user import User  # ← indispensable

async def init_models():
    async with engine.begin() as conn:
        print("🔧 Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created successfully.")

asyncio.run(init_models())