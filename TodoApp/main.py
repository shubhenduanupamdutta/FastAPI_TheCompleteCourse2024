import models
from database import engine
from fastapi import FastAPI
from routers import admin, auth, todo

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Will only run once and if only the database is not created

app.include_router(auth.router, prefix="/auth", tags=["Authentications"])
app.include_router(todo.router, prefix="/todo", tags=["Todo"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
