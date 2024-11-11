# import models
# from database import engine
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .routers import admin, auth, todo, users

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)  # Not needed after using Alembic
# Will only run once and if only the database is not created

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router, prefix="/auth", tags=["Authentications"])
app.include_router(todo.router, prefix="/todo", tags=["Todo"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(users.router, prefix="/user", tags=["User"])
