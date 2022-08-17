from db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Users(db.Document):
    '''
    Users database schema
    '''
    
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    age = db.IntField()
    created_on = db.DateTimeField()
    last_logged_on = db.DateTimeField(Default=None)

    def hash_password(self):
        self.password = generate_password_hash(self.password, 10).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
