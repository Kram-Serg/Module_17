from fastapi import FastAPI
from router import task
from router import user

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_raleouter(user.router)