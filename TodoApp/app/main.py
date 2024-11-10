# import models
# from database import engine
from fastapi import FastAPI
from .routers import admin, auth, todo, users

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)  # Not needed after using Alembic
# Will only run once and if only the database is not created


@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router, prefix="/auth", tags=["Authentications"])
app.include_router(todo.router, prefix="/todo", tags=["Todo"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(users.router, prefix="/user", tags=["User"])
