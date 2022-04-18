from .repository import fetch_users, insert_user
from .models import User


def read_users():
    return fetch_users()


def add_user(user: User):
    insert_user(user)
