from genericpath import isfile
import os, glob
import unittest

from API.models.user import User
from API.models.file import File
from API.database.fileCollection import ClearFileCollection
from API.database.userCollection import ClearUserCollection, AddRecievedFileByUsername, CreateNewUser
from tests.controllersTests.fileControllerTests import FileControllerTests
from tests.controllersTests.userControllerTests import UserControllerTests

 
python_file_paths = []
current_directory = os.getcwd()

users = [User("username1", "password").setObjectID("user_id"), User("username2", "password"), User("username3", "password")]
file_data = File("sample_file_name", users[0]).setObjectID("Sample_object_id")

def PrepareMongoDBDatabase():
    ClearUserCollection()
    ClearFileCollection()
    
    for user in users:
        CreateNewUser(user)
        AddRecievedFileByUsername(file_data, user.getUser())

def suite():
    controller_suite = unittest.TestSuite()
    controller_suite.addTest(UserControllerTests())
    controller_suite.addTest(FileControllerTests())
    return controller_suite

if  __name__ == '__main__':
    PrepareMongoDBDatabase()
    python_file_paths = []

    for root, directories, files in os.walk(current_directory + "/tests", topdown=True):
        for dir in directories:
            directory_path = current_directory + "/tests/{0}".format(dir)
            files = os.listdir(directory_path)

            for file in files:
                file_path = "{0}/{1}".format(directory_path, file)
                file_extension = os.path.splitext(file_path)[1]

                if (isfile(file_path) & (file_extension == ".py")):
                    file_path = file_path.replace(current_directory +"/", "")
                    python_file_paths.append(file_path)
    
    for file_path in python_file_paths:
        print("Excecuting file : {0}".format(file_path))
        exec(open(file_path).read())

            
                    
                    


