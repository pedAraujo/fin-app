from ..mongo import db
from app import login_manager


class User:
    def __init__(self, username, first_name, email, _id):
        self.username = username
        self.first_name = first_name
        self.email = email
        self._id = _id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id


@login_manager.user_loader
def load_user(username):
    user = db.users.find_one({"username": username})
    if not user:
        return None
    return User(
        user["username"],
        user["first_name"],
        user["email"],
        user["_id"],
    )
