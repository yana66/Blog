from . import *


def salted_password(password):
    salt = 'adsaiefs'
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
        query.update(created_time=time.time(), password=password, deleted=False)
        mongo[name].insert(query)

    @classmethod
    def register(cls, form):
        username = form.get('username')
        if User.find_one(username=username):
            return False
        else:
            User.new(form)
            return True

    @classmethod
    def login(cls, form):
        username = form.get('username')
        password = form.get('password')
        user = User.find_one(username=username)

        if user and user['password'] == salted_password(password):
            return user
        else:
            return None