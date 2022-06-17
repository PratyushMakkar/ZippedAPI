from dotenv import load_dotenv
import os
import pyrebase


load_dotenv()

config = {
  "apiKey": os.environ.get("apiKey"),
  "authDomain": os.environ.get("authDomain"),
  "databaseURL": os.environ.get("databaseURL"),
  "storageBucket": os.environ.get("storageBucket"),
  "serviceAccount": os.environ.get("serviceAccount")
}

username = os.environ.get("gmail_username")
password = os.environ.get("gmail_password")

def IntializeFirebaseApp():
  firebase = pyrebase.initialize_app(config)
  return firebase

def IntializeFirebaseAuth():
  auth = IntializeFirebaseApp().auth()
  return auth

def IntializeFirebaseStorage():
  firebaseBucket = IntializeFirebaseApp().storage()
  return firebaseBucket

def CreateAuthUser():
  return IntializeFirebaseAuth().sign_in_with_email_and_password(username, password)