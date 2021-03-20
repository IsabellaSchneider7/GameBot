from firebase import firebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
  "apiKey": os.getenv('API_KEY') ,
  "authDomain": os.getenv('AUTH_DOMAIN'),
  "storageBucket": os.getenv('STORAGE_BUCKET'),
  "databaseURL": os.getenv('DATABASE_URL'),
}

firebase = firebase.FirebaseApplication("https://gamebot-ccab1-default-rtdb.firebaseio.com", None)

