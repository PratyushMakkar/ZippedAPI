from firebase_admin.storage import bucket
from fastapi import UploadFile
from API.database.firebaseConfig import IntializeFirebaseStorage
from API.models.file import File
#from API.database.firebaseConfig import CreateAuthUser


bucket = IntializeFirebaseStorage()
#user = CreateAuthUser()

def UploadFileToStorage(file_data: File, file):

    filename = file_data.getFileName()
    owner = file_data.getFileOwner().getUser()

    file_path = "{0}/{1}".format(owner, filename)
    blob = bucket.blob(file_path)
    response_object = blob.upload_from_file(file); blob.make_public()

    download_url = blob.public_url
    return (response_object, download_url)
    
def DeleteFileFromStorage():
    pass


