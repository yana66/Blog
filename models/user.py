from . import *
from config import salt


def salted_password(password):
    import hashlib
    hash1 = hashlib.md5(password.encode('ascii')).hexdigest()
    hash2 = hashlib.md5((hash1 + salt).encode('ascii')).hexdigest()
    return hash2


class User(Mongo):
    @classmethod
    def new(cls, form):
        password = salted_password(form.get('password'))
        name = cls.__name__.lower()
        query = {k: v for k, v in form.items()}
        query.update(created_time=time.time(), password=password, deleted=False, admin=False)
        mongo[name].insert(query)

    @classmethod
    def register(cls, form):
        username = form.get('username')
        if cls.find_one(username=username):
            return False
        else:
            cls.new(form)
            return True

    @classmethod
    def login(cls, form):
        username = form.get('username')
        password = form.get('password')
        user = cls.find_one(username=username)
        if user and user['password'] == salted_password(password):
            return user
        else:
            return None

