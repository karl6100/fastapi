
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#from alembic.config import Config
#from alembic import command


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def run_migrations():
#     alembic_cfg = Config("alembic.ini")
#     command.upgrade(alembic_cfg, "head")

# # Call this function in the startup section of your app
# run_migrations()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my API!!!"}



