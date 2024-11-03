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
def get_user(request: Request, user_id: Annotated[int, Path(description="ID пользователя")]) -> HTMLResponse:
    try:
        user = users[user_id - 1]
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(description="Имя пользователя")],
                age: Annotated[int, Path(description="Возраст пользователя")]) -> User:
    if users:
        new_id = users[-1].id + 1
    else:
        new_id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: Annotated[int, Path(description="ID пользователя")],
                username: Annotated[str, Path(description="Имя пользователя")],
                age: Annotated[int, Path(description="Возраст пользователя")]) -> User:
    try:
        edit_user = next(user for user in users if user.id == user_id)
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: Annotated[int, Path(description="ID пользователя")]) -> User:
    try:
        user_del = next(user for user in users if user.id == user_id)
        users.remove(user_del)

        for i, user in enumerate(users):
            user.id = i + 1
        return user_del
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")
