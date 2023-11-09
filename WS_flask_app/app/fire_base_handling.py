import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from hashlib import sha256

class firebase:
    def __init__(self):
        self.FIREBASE_CREDENTIALS = credentials.Certificate('firebaseJSON.json')


    def init_firebase(self):
        app = firebase_admin.initialize_app(self.FIREBASE_CREDENTIALS)
        self.db = firestore.client()
        return self.db


class fire_base_handling:
    def __init__(self):
        self.db = firebase().init_firebase()

    def create_user_object(self,name="",passcode=""):
        d={}
        # name=input("name : ")
        d['name']=name
        # passcode=maskpass.askpass(prompt=, mask="*")
        # passcode=input(f"Passcode:\n(min 8 digit/char) : ")
        # d['passcode']=passcode
        hash_gen=str(passcode[:4])+name+str(passcode[4:])
        hash_gen=sha256(hash_gen.encode())
        
        d['key_XV']=hash_gen.hexdigest()
        print(f"User '{name}' is created")
        return d

    def create_user(self,username="",passcode=""):
        user_data=self.create_user_object(username,passcode)
        doc_ref = self.db.collection("Users").document(user_data['name'])
        doc_ref.set(user_data)
        print("Added user")
        return(user_data['key_XV'])

    def read_user_spec(self,user=""):
        users_ref = self.db.collection("Users").document(f'{user}')
        # data=users_ref.stream()
        return users_ref.get().to_dict()

    def update_user_spec(self,user="",update_data={}):
        users_ref = self.db.collection("Users").document(f'{user}').update(update_data)

    def hash_gen(self,user=''):
        data=read_user_spec(user)
        passc=data['passcode']
        name=data['name']
        hgen=str(passc[:4])+name+str(passc[4:])
        hgen_key=sha256(hgen.encode())
        return hgen_key.hexdigest()


# if __name__=="__main__":
#     print("This is a module. Run the main.py file")
#     print(fire_base_handling().create_user('hi','1234567890'))