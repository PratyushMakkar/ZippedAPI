from array import array
import inspect
from itertools import filterfalse
from typing_extensions import assert_type
import unittest
from dotenv import load_dotenv
import requests
import os

from API.models.user import User
from API.database.userCollection import VerifyUser

load_dotenv()

user = User("username", "password")
user_one= User("username1", "password").setObjectID("user_id")
SERVER_URL = os.environ.get("SERVER_URL") + "/user"

class UserControllerTests(unittest.TestCase):

    def test_createNewUserControllerTest(self):     
        response = requests.post(SERVER_URL,                    #test for when the user does not exist in the database
        json=                    
            {
                'username': user.getUser(),
                'password': user.getPassword()
            }
        )
        print(response)
        assert(response.status_code == 200)
        assert(VerifyUser(user))

        json_response = response.json()
        assert(json_response['_id'] is not None)
        assert(json_response['user'] == user.getUser())

    def test_alreadyExistingUserControllerTest(self):             #test for when the user already exists in the database
        response = requests.post(SERVER_URL,
        json =
            {
                'username': user_one.getUser(),
                'password': user_one.getPassword()
            }
        )
        assert(response.status_code == 405)

    def test_searchUserControllerTest(self):
        response = requests.get(SERVER_URL + "/search", json=
            {
                'username': user_one.getUser(),
                'password': user_one.getPassword()
            }
        )
        assert(response.status_code == 200)

        json_response = response.json()
        assert(json_response['_id'] is not None)
        assert(json_response['user'] == user_one.getUser())

    def test_searchMissingUserControllerTest(self):
        response = requests.get(SERVER_URL + "/search",
        json=
            {
                'username': "FalseUser",
                'password': user_one.getPassword(),
                'object_id': "FalseObject_ID"
            }
        )
        assert(response.status_code == 404)
    
    def test_searchRecievedFilesControllerTest(self):
        response = requests.get(SERVER_URL + "/recievedFiles",
        json =
            {
                'username': user_one.getUser(),
                'password': user_one.getPassword(),
                'object_id': user_one.getObjectID()
            } 
        )
        assert(response.status_code == 200)

        json_response = response.json()
        assert(json_response['recievedFiles'] is not None)
        assert(json_response['recievedFiles'][0][0]=="Sample_object_id")
    
    def test_malformedSearchRecievedFilesControllerTest(self):
        response = requests.get(SERVER_URL + "/recievedFiles",
        json= 
            {
                'username': "FalseUser",
                'password': user_one.getPassword(),
                'object_id': "FalseObject_ID"
            } 
        )
        assert(response.status_code == 404)

    def test_downloadFileControllerTest(self): 
        pass

if __name__ == '__main__':
    unittest.main()