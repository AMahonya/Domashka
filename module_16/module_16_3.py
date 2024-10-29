from typing import Annotated

from fastapi import FastAPI, Path
from pyexpat.errors import messages

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    current_id = str(int(max(users, key=int)) + 1)
    users[current_id] = f"Имя: {username}, возраст: {age}"
    return f"User {current_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} is deleted"