from msilib.schema import Patch

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, status, Body, HTTPException, Request, Form, Path
from pydantic import BaseModel
from typing import List
from typing import Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}')
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


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
