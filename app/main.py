from fastapi import Depends, FastAPI
from routers import users, token, messages
from sql_app import models
from sql_app.database import engine, SessionLocal


# db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(token.router)
app.include_router(messages.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

