from http.client import HTTPException
import re
import traceback
from xmlrpc.client import Boolean
from API.database.databaseConfig import createUserCollection
from API.models.user import User
from API.models.file import File
import json
import bson

user_collection = createUserCollection()

def VerifyUser(user: User) -> bool:                         # Used in Authentication to verify if the user with name 
    user_object = user_collection.find_one(         # and password exists in the database
        {
            "user": user.getUser(),
            "password": user.getPassword()
        }
    )
    if (user_object==None):
        return False
    return True

def UserExistsByUsername(username: str):            # Checks within the database if the username already exists
    user_object = user_collection.find_one(        
        {
            "user": username
        }
    )
    if (user_object==None):
        return False
    return True

def FindUserByObjectId(object_id: str):
    user_object = user_collection.find_one(        
        {
            "_id": object_id
        }
    )
    return user_object

def FindUserByUsername(username: str):
    user_object = user_collection.find_one(        
        {
            "user": username
        }
    )
    return user_object

def CreateNewUser(user: User):                       # Method used to create a new user using user and password
    username = user.getUser()
    user_password = user.getPassword()

    if (UserExistsByUsername(user.getUser())):
        return None
    else:
        user_object = user_collection.insert_one(
            {
                'user': user.getUser(),
                'password': user.getPassword(),
                'recievedFiles': []
            }
        )
        if (user_object.acknowledged):
            return FindUserByObjectId(user_object.inserted_id)
        return None
    

def UserExistsByObjectID(id: str):                      # Method used to check if an object ID belongs to some user
    user_object = user_collection.find_one(        
        {
            "_id": id
        }
    )
    if (user_object == None):
        return False
    return True

def AddRecievedFileByUsername(file: File, username: str):   # Method to add a file to a username
    if (UserExistsByUsername(username)):
        user_object = user_collection.update_one(
            {'user': username},
            {
                '$push': {
                    'recievedFiles': file.getObjectID()
                }
            }
        )
        return user_object.acknowledged
    return False
    
def ViewRecievedFilesByUser(username: str):                    # Method to list all files recieved by the User
    if (UserExistsByUsername(username)):
        user_object = user_collection.find_one(
            {
                'user': username
            }
        )
        return user_object['recievedFiles']
    return None

def ViewRecievedFilesByObjectID(object_id: str):                    # Method to list all files recieved by the User
    if (UserExistsByObjectID(object_id)):
        user_object = user_collection.find_one(
            {
                '_id': object_id
            }
        )
        try: 
            return user_object['recievedFiles']
        except KeyError as err:
            print("Missing Key: 'recievedFiles")
            print(traceback.print_exception(err))
    return None

def FindObjectIdByUsernames(usernames: list):           
    user_id_array= []

    for user_id in usernames:
        user_object = user_collection.find_one({'user': user_id})
        if (user_object is not None):
            object_id = json.loads(user_object)['_id']
            user_id_array.append(object_id)

    return user_id_array

def ClearUserCollection():
    response = user_collection.delete_many({})
    print("Deleted {0} documents from the user collection".format(response.deleted_count))

    
