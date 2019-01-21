from vedis import Vedis
from config import States, db_file


def get_current_state(user_id):
    with Vedis(db_file) as db:
        try:
            db_userId = db[user_id]
            db_userId = str(db_userId, 'utf-8')
            print(type(db_userId))
            return db_userId
        except KeyError:
            return States.S_START.value


def set_state(user_id, value):
    with Vedis(db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False