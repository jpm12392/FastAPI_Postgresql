from fastapi import FastAPI
from db_utils import db  # Import the database instance

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.get("/")
async def blogs():
    query = "SELECT * FROM blogs"
    rows = await db.fetch(query)
    if rows:
        return rows
    return {"detail": "No blogs found"}
