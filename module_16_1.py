from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("Главная страница")

@app.get("/user/admin")
async def admin_user():
    return HTMLResponse("Вы вошли как администратор")

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return HTMLResponse(f"Вы вошли как пользователь № {user_id}")

@app.get("/user")
async def get_user_info(request: Request):
    username = request.query_params.get("username")
    age = request.query_params.get("age")
    if username and age:
        return HTMLResponse(f"Информация о пользователе. Имя: {username}, Возраст: {age}")
    else:
        return HTMLResponse("Недостаточно данных для отображения информации о пользователе")


# uvicorn module_16_1 --reload