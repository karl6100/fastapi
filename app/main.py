
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='M@$t3rM!nd', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was Successful!")
#         break
#     except Exception as error:
#         print("Database connection failed!")
#         print("Error", error)
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "welcome to my API"}



