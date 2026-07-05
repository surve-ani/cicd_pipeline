#owner  - Aniket


from fastapi import FastAPI
from routers.user import router as user_router

app = FastAPI(title="My First FastAPI App")

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

app.include_router(user_router)