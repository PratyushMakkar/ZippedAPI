import traceback
from API.database.databaseConfig import createFilesCollection
from API.database.databaseConfig import createUserCollection
from API.models.user import User
from API.models.file import File
import json

files_collection = createFilesCollection()

def FileExistsByID(file_id: str):
    if (files_collection.find_one({"_id": file_id}) != None):
        return True
    return False

def CreateNewFileRecord(file: File):

    file_object = files_collection.insert_one(
        {
            'name': file.getFileName(),
            'owner': file.getFileOwner().getUser(),
            'recipients': file.getFileRecipients(),
            'url': file.getFileURL(),          
        }
    )
    return file_object

def FindFileByID(object_id: str):

    if (FileExistsByID(object_id)):
        file_object = files_collection.find_one(
            {
                '_id': object_id
            }
        )
        return file_object
    return None

def DeleteFileRecord(object_id: str):

    if (FileExistsByID(object_id)):
        file_object = files_collection.find_one_and_delete(
            {
               "_id": object_id 
            }
        )
        return file_object
    return None

def GetFileDownloadURL(object_id: str):

    if (FileExistsByID(object_id)):
        file_object = files_collection.find_one(
            {
             "_id": object_id 
            }
        )
        return file_object['url']
    return None

def ClearFileCollection():
    response = files_collection.delete_many({})
    print("Deleted {0} documents from the files collection".format(response.deleted_count))