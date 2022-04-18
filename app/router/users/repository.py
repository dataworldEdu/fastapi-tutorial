from .models import User, UserList
userdata = [
    {"user_id": "john", "user_name": "John", "age": 26, "birthday": "19860711"},
]


def fetch_users():
    users = UserList(__root__=userdata)
    return users


def insert_user(user: User):
    pass

