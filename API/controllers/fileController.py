from fastapi import HTTPException
from fastapi import APIRouter, UploadFile, File

from API.controllers.requestModels import FileUploadRequestModel
from API.models.user import User
from API.models.file import File as _File
from API.businessLogic.fileControllerLogic import UploadFileObject

router = APIRouter(
    prefix = "/files",
    tags = ["files"]
)

@router.post("/")
def UploadFileController(file: UploadFile = File(...)):
    '''
    owner_username = fileRequest.owner_username
    owner_password = fileRequest.owner_password
    filename = fileRequest.filename
    recipients = fileRequest.reciepients
    user = User(owner_username, owner_password)
    
    file_data = File(filename, user).setFileRecipients(recipients)
    
    return UploadFileObject(file_data, file)
    '''
    return file.content_type

@router.delete("/")
def DeleteFileController(fileRequest: FileUploadRequestModel):
    if (fileRequest.object_id is None):
        raise HTTPException(status_code= 403, detail= "The file object ID is missing")
    return {"user": "user", "password": "password"}

