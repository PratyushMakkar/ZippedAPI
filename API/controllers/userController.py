from fastapi import APIRouter, FastAPI

from API.controllers.requestModels import UserRequestModel
from API.businessLogic.userControllerLogic import CreateNewUserObject, SearchRecievedFilesObject, SearchUserObject
from API.models.user import User
from API.controllers.requestModels import FileDownloadRequestModel
from API.models.file import File
from API.businessLogic.fileControllerLogic import GetDownloadURLObject

router = APIRouter(
    prefix = "/user",
    tags = ["user"]
)

@router.post("/")
async def CreateNewUserController(userRequest: UserRequestModel):
    password = userRequest.password
    username = userRequest.username
    user = User(username, password)

    return CreateNewUserObject(user)                  #Handled in businessLogic.userControllerLogic

@router.get("/search")
async def SearchUserController(userRequest: UserRequestModel):
    username = userRequest.username
    password = userRequest.password
    object_id = userRequest.object_id
    user = User(username, password).setObjectID(object_id)

    return SearchUserObject(user)                        #Handled in businessLogic.userControllerLogic

@router.get("/recievedFiles")
async def SearchRecievedFilesController(userRequest: UserRequestModel):
    username = userRequest.username
    password = userRequest.password
    object_id = userRequest.object_id
    user = User(username, password).setObjectID(object_id)

    return SearchRecievedFilesObject(user)               #Handled in businessLogic.userControllerLogic

@router.get("/downloadFile")
async def DownloadFileController(userRequest: FileDownloadRequestModel):
    username = userRequest.client_username
    password = userRequest.client_password
    user = User(username, password)

    filename = userRequest.filename
    object_id = userRequest.object_id
    file_data = File(filename, user).setObjectID(object_id)
    return GetDownloadURLObject(file_data, user)








