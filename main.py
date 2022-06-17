from dotenv import load_dotenv
import uvicorn
import os

from fastapi import APIRouter, FastAPI

from API.controllers.userController import router as userRouter
from API.controllers.fileController import router as fileRouter

load_dotenv(".env")
host_ip = os.environ.get("production_ip")
port = os.environ.get("production_port")

app = FastAPI()
app.include_router(userRouter)
app.include_router(fileRouter)


@app.get("/")
async def root():
	return {"message": "The App works!"}


if __name__ == "__main__":
	uvicorn.run(app)
