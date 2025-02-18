import firebase_admin
from firebase_admin import db

class firebase():
    def __init__(self):
    
        cred_obj = firebase_admin.credentials.Certificate('credentials.json')
        default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL':"https://findteammates-38ac1-default-rtdb.asia-southeast1.firebasedatabase.app/"
            })

    def add_user(self,data):
        ref=db.reference("/")
        ref.child("mails").push(data["mail"])
        ref.child("users").child(data["name"]).set({"name":data["name"],"password":data["password"],"contact":data["contact"]})
    #ref.get()

