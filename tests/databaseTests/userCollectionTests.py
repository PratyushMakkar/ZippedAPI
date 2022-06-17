import unittest
from API.models.user import User
from API.models.file import File
from API.database.userCollection import AddRecievedFileByUsername, CreateNewUser, UserExistsByObjectID, UserExistsByUsername, VerifyUser, ViewRecievedFilesByUser
from tests.testing_script import users

user = users[0]
file = File("harrpotter", user)
file.setObjectID("IDNew")
file.setFileURL("URL")
file.setFileRecipients(["user2", "user3"])

class UserCollectionTests(unittest.TestCase):

    def test_createUserTest(self):
        user_object = CreateNewUser(user)

        if (user_object!=None):
            user_object_id = user_object['_id']
            assert(UserExistsByUsername(user.getUser()))
            assert(UserExistsByObjectID(user_object_id))

    def test_verifyUserTrueTest(self):
        assert(VerifyUser(user))
        
    def test_verifyUserFalseTest(self):
        assert(not VerifyUser(User("user1", "false_password")))

    def test_userExistsByUsernameTest(self):
        assert(UserExistsByUsername(user.getUser()))

    def test_addingRecievedFileTest(self):
        recieved_object = AddRecievedFileByUsername(file, user.getUser())
        assert(recieved_object is not False)
        assert(file.getObjectID() in ViewRecievedFilesByUser(user.getUser()))


if __name__ == '__main__':
    unittest.main()

