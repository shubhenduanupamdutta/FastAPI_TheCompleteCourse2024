import models
from database import engine
from fastapi import FastAPI
from routers import auth, todo

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Will only run once and if only the database is not created

app.include_router(auth.router, tags=["Authentications"], prefix="/auth")
app.include_router(todo.router, tags=["Todos"], prefix="/todos")
