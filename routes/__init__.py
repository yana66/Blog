from flask import session, request, url_for, redirect, render_template, Blueprint, abort
from models.user import User
from models.post import Post
from functools import wraps
import time


def current_user():
    username = session.get('username')
    user = User.find_one(username=username)
    return user


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        u = current_user()
        if u is None:
            return redirect(url_for('home.auth'))
        return f(*args, **kwargs)
    return function


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        username = session.get('username')
        user = User.find_one(username=username, admin=True)
        if not user:
            return "对不起,权限不足不能发表博客"
        return f(*args, **kwargs)
    return function