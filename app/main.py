from fastapi import FastAPI, HTTPException
from models import database, users
from schema import User, UserCreate

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    query = "INSERT INTO users (name, email) VALUES (:name, :email) RETURNING id"
    values = {"name": user.name, "email": user.email}
    last_record_id = await database.execute(query=query, values=values)
    return {**user.dict(), "id": last_record_id}

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :id"
    user = await database.fetch_one(query=query, values={"id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 10):
    query = "SELECT * FROM users OFFSET :skip LIMIT :limit"
    users = await database.fetch_all(query=query, values={"skip": skip, "limit": limit})
    return users

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    query = "UPDATE users SET name = :name, email = :email WHERE id = :id RETURNING *"
    values = {"id": user_id, "name": user.name, "email": user.email}
    updated_user = await database.fetch_one(query=query, values=values)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = :id RETURNING id"
    deleted_user_id = await database.execute(query=query, values={"id": user_id})
    if deleted_user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": deleted_user_id}
