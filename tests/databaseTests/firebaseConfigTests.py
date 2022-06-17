
import unittest

from fastapi import File, UploadFile
from API.database.firebaseConfig import IntializeFirebaseStorage, IntializeFirebaseApp
import pyrebase 
import os

from API.database.blobFileStorage import UploadFileToStorage


storage = IntializeFirebaseStorage()
currentPath = os.getcwd()

class FirebaseConfigTests(unittest.TestCase):

    def test_uploadFirebaseFile(self):
        file = File()
        
    def test_deleteFirebaseFile(self):
        storage.child("data/").delete("j")
        
    def test_findFileByIDTest(self):
        pass
        

if __name__ == '__main__':
    unittest.main()