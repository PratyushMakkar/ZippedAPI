from array import array
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    username: str
    password: str
    object_id: Union[str, None] = None

class FileUploadRequestModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    owner_username: str
    owner_password: str
    filename: str
    reciepients: array
    object_id: Union[str, None] = None
    media_type: Union[str, None] = None

class FileDownloadRequestModel(BaseModel):
    client_username: str
    client_password: str
    filename: str
    object_id: str
    media_type: Union[str, None] = None