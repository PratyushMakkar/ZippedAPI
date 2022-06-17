import unittest
import sys,os

from API.database.databaseConfig import createDatabase, createFilesCollection, createUserCollection

class ConnectionTests(unittest.TestCase):

    def test_databaseExistsTest(self):
        assert(createDatabase() != -1)

    def test_collectionExistsFileTest(self):
        collection_name = os.environ.get('file_collections_name')
        db = createDatabase()
        collections_list = db.list_collection_names()
        assert(collection_name in collections_list)

    def test_collectionExistsUserTest(self):
        collection_name = os.environ.get('user_collections_name')
        db = createDatabase()
        collections_list = db.list_collection_names()
        assert(collection_name in collections_list)

if __name__ == '__main__':
    unittest.main()


