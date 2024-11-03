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
def create_user(username: str, age: int) -> User:
    if users:
        new_id = users[-1].id + 1
    else:
        new_id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = next(user for user in users if user.id == user_id)
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: int) -> User:
    try:
        user_del = next(user for user in users if user.id == user_id)
        users.remove(user_del)
        return user_del
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")
