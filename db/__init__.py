from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    '''
    Initializing database connection
    '''
    db.init_app(app)