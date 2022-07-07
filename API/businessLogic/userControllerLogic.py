from array import array
from distutils.log import error
from multiprocessing.dummy import Array
import traceback
from API.models.user import User
from API.database.userCollection import CreateNewUser

from fastapi import HTTPException

from API.database.userCollection import FindUserByObjectId, FindUserByUsername, ViewRecievedFilesByObjectID, ViewRecievedFilesByUser
from API.database.fileCollection import FindFileByID

def CreateNewUserObject(user: User):
    response_object = CreateNewUser(user)

    if (response_object is None):
        raise HTTPException(status_code= 405, detail= "Method not allowed. The user with the specified username already exists in the database")
    return response_object

def SearchRecievedFilesObject(user: User):
    response_object = ViewRecievedFilesByUser(user.getUser())

    if (response_object is None):
        response_object_id = ViewRecievedFilesByObjectID(user.getObjectID())

        if (response_object_id is None):
            raise HTTPException(status_code= 404, detail= "The user or the user files could not be located in the database")
        return FindFilenamesFromID(response_object_id)

    return {
        'recievedFiles': FindFilenamesFromID(response_object)
    }

def SearchUserObject(user: User):
    response_object = FindUserByUsername(user.getUser())
    
    if (response_object is None):
        response_object_id = FindUserByObjectId(user.getObjectID())

        if (response_object_id is None):
            raise HTTPException(status_code= 404, detail= "The user could not be located in the database")
        return response_object_id

    return response_object 
            
def FindFilenamesFromID(files_array: array):
    for i, file_id in enumerate(files_array):
        try:
            file = FindFileByID(file_id)
            if (file):
                files_array[i] = {
                    'id': file_id, 
                    'name': file['name'], 
                    'url': file['url'], 
                    'owner': file['owner']
                }
        except TypeError as err:
            files_array[i] = (file_id, "")
            print(traceback.print_exception(err))
    return files_array