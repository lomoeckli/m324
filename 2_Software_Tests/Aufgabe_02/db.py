from pymongo import MongoClient
from user import User

class Db:
    def __init__(self, connection_string: str):
        self.client = MongoClient(connection_string)
        self.db = self.client["test_db"]
        self.collection = self.db["users"]

    def set_user(self, user: User):
        user_data = {
            "name": user.name,
            "mail": user.mail
        }
        self.collection.insert_one(user_data)

    def get_user(self) -> User:
        data = self.collection.find_one()
        if data is None:
            return None

        return User(
            name = data["name"],
            mail = data["mail"]
        )
