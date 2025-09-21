import asyncio
import aiosqlite

async def async_fetch_users():
    """Fetch all users asynchronously."""
    async with aiosqlite.connect("mydb.sqlite3") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect("mydb.sqlite3") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    """Run both queries concurrently using asyncio.gather."""
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All Users:", users)
    print("Users older than 40:", older_users)

# ✅ Run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
