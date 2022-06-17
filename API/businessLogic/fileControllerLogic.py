import traceback
from fastapi import HTTPException
from fastapi import UploadFile
from grpc import StatusCode
from pydantic import NoneIsNotAllowedError
from API.models.file import File
from API.database.blobFileStorage import UploadFileToStorage
from API.models.user import User
from API.database.fileCollection import CreateNewFileRecord, GetFileDownloadURL
from API.database.userCollection import AddRecievedFileByUsername
from API.database.userCollection import VerifyUser, ViewRecievedFilesByUser

def UploadFileObject(file_data: File, file: UploadFile):

    client = file_data.getFileOwner()
    if (not VerifyUser(client)):
        raise HTTPException(404, detail= "Could not locate User with username: {0} and password {1}"
        .format(client.getUser, client.getPassword))

    try:
        (result, download_url) = UploadFileToStorage(file)
    except:
        raise HTTPException(StatusCode = 404, detail= "Could not upload file to the database")
    
    try:
        if (download_url is None):
            raise HTTPException(StatusCode = 404, detail= "Could not locate the URL of the uploaded file")
        else:
            file_url = download_url
            file_data = file_data.setFileURL(file_url)
            file_object = CreateNewFileRecord(file_data)

    except Exception as err: 
        print("Error Occured: {0}".format(err))
        print(traceback.print_exception(err))
        return

    for user in file_object['recipients']:
        response = AddRecievedFileByUsername(file_data, user)
        if (response is False):
            raise HTTPException(StatusCode = 404, detail= "Could not find the recipient: {0} of the file".format(user))


def GetDownloadURLObject(file_data: File, client: User):

    if (not VerifyUser(client)):
        raise HTTPException(404, detail= "Could not locate User with username: {0} and password {1}"
        .format(client.getUser, client.getPassword))
    
    object_id = file_data.getObjectID()
    username = client.getUser()

    try: 
        if (not VerifyUserHasAccessToFile(object_id, client)):
            raise HTTPException(403, detail= "Could not veryify access to file with object_id: {0}".format(object_id))
    except NoneIsNotAllowedError as err:
        print("Could not find the user with username:{0}".format(username))

    try: 
        response_object = GetFileDownloadURL(object_id)
    except KeyError as err:
        print("Error Occured :{0}".format(err), "Missing Key: 'url'")
        print(traceback.print_exception(err))
        raise HTTPException(500, detail= "There was an internal servor key error while prcoessing a JSON")
    return response_object


def VerifyUserHasAccessToFile(object_id: str, user: User):
    if (user.getUser() is None):
        raise NoneIsNotAllowedError()

    try: 
        user_files = ViewRecievedFilesByUser(user.getUser())
    except Exception as err:
        print("Error occured: {0}".format(err)) 

    if (object_id in user_files):
        return True
    return False

    