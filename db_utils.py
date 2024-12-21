import asyncpg
from typing import Any, List, Dict

DATABASE_URL = "postgresql://postgres:Maurya%4012345@127.0.0.1:5432/mvpdb"

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch(self, query: str, *args: Any) -> List[Dict]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch(query, *args)
            return [dict(row) for row in rows]

    async def fetch_one(self, query: str, *args: Any) -> Dict:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow(query, *args)
            return dict(row) if row else None

    async def execute(self, query: str, *args: Any) -> None:
        async with self.pool.acquire() as connection:
            await connection.execute(query, *args)

# Create a single instance of the Database class
db = Database()
