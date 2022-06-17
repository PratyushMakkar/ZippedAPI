import re
from fastapi import UploadFile
from API.database.firebaseConfig import IntializeFirebaseStorage
from API.models.file import File
from API.database.firebaseConfig import IntializeFirebaseAuth, CreateAuthUser


storage = IntializeFirebaseStorage()
bucket = storage.bucket
user = CreateAuthUser()

def UploadFileToStorage(file_data: File, file):

    filename = file_data.getFileName()
    owner = file_data.getFileOwner().getUser()

    file_path = "{0}/{1}".format(owner, filename)

    response_object = storage.child(file_path).put(file, user['idToken'])
    download_url = storage.child(file_path).get_url(response_object['downloadTokens'])
    return (response_object, download_url)
    
def DeleteFileFromStorage():
    pass


