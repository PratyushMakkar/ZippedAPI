from dotenv import dotenv_values, load_dotenv
import os
from pymongo import MongoClient

load_dotenv(".env")
database_url = os.environ.get('database_url')
user_string= os.environ.get('user')
password= os.environ.get('password') 
db_name = os.environ.get('db_name')

client = MongoClient(database_url)

def createDatabase():
    db_names = client.list_database_names()
    if db_name in db_names:
        return client[db_name]

def createFilesCollection():
    db = createDatabase()
    file_collections_name = os.environ.get('file_collections_name')
    return db.get_collection(file_collections_name)

def createUserCollection():
    db = createDatabase()
    user_collections_name = os.environ.get('user_collections_name')
    return db.get_collection(user_collections_name)



