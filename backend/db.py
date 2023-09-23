import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

firebaseConfig = {
    'apiKey': "AIzaSyCrAA9gVJJp3CEw6pOXlIIrZiBEPBY28X0",
    'authDomain': "kiwkiw-833f3.firebaseapp.com",
    'databaseURL': "https://kiwkiw-833f3-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "kiwkiw-833f3",
    'storageBucket': "kiwkiw-833f3.appspot.com",
    'messagingSenderId': "205836361621",
    'appId': "1:205836361621:web:ca648d5e4497c18b79609c"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()