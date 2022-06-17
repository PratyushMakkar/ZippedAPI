import unittest
from API.models.user import User
from API.models.file import File
from API.database.fileCollection import FileExistsByID
from API.database.fileCollection import CreateNewFileRecord, DeleteFileRecord

user = User("user1", "password1")
file = File("harrpotter", user)
file.setObjectID("IDNew")
file.setFileURL("URL")
file.setFileRecipients(["user2", "user3"])


class FileCollectionTests(unittest.TestCase):

    def test_createFileRecordTest(self):
        file_object = CreateNewFileRecord(file)
        assert(file_object.acknowledged)
        assert(FileExistsByID(file_object.inserted_id))

    def test_deleteFileRecordTest(self):
        file_object = CreateNewFileRecord(file.setFileURL("Yaya"))
        assert(DeleteFileRecord(file_object.inserted_id)is not None)
        assert(not FileExistsByID(file_object.inserted_id))
        
    def test_findFileByIDTest(self):
        file_object = CreateNewFileRecord(file.setFileURL("SampleURl"))
        assert(FileExistsByID(file_object.inserted_id))

if __name__ == '__main__':
    unittest.main()