from flask import session, request, url_for, redirect, render_template, Blueprint
from models.user import User
from models.post import Post
import time


def current_user():
    username = session.get('username')
    user = User.find_one(username=username)
    return user


