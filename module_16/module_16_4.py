from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return f"{user} Регистрация прошла успешна!"


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"{edit_user} Данные успешно обнавлены!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User {users} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
