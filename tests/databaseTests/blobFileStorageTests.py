from typing import BinaryIO
import unittest

from fastapi import UploadFile
from API.models.file import File
from API.models.user import User


from API.database.blobFileStorage import UploadFileToStorage

sample_file = open("utils/testFile.txt")
file_data = File("testFile.txt", User("username", "password"))

class BlogFileStorageTests(unittest.TestCase):
    
    def test_UploadFileResult(self):
        (response_object, download_url) = UploadFileToStorage(file_data= file_data, file = sample_file)
        assert(response_object is not None)
        assert(download_url is not None)
    
if __name__ == '__main__':
    unittest.main()