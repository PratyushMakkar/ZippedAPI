from dotenv import load_dotenv
import os
import firebase_admin
import firebase_admin.storage as storage
from firebase_admin import auth
from httplib2 import Credentials

load_dotenv()

config = {
  "apiKey": os.environ.get("apiKey"),
  "authDomain": os.environ.get("authDomain"),
  "databaseURL": os.environ.get("databaseURL"),
  "storageBucket": os.environ.get("storageBucket"),
  "serviceAccount": os.environ.get("serviceAccount")
}

_USER_ID = os.environ.get("USER_ID")
username = os.environ.get("gmail_username")
password = os.environ.get("gmail_password")
_CREDENTIAL = os.environ.get("serviceAccount")

def IntializeFirebaseApp():
  _credential = firebase_admin.credentials.Certificate(_CREDENTIAL)
  firebase = firebase_admin.initialize_app(credential = _credential, name = config['storageBucket'])
  return firebase

def IntializeFirebaseStorage():
  app = IntializeFirebaseApp()
  firebaseBucket = storage.bucket(name = config["storageBucket"], app = app)
  assert(firebaseBucket); "The firebase bucket cannot be a null object"
  return firebaseBucket
  
'''
def CreateAuthUser():
  return auth.get_user(_USER_ID)
'''