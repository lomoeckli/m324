import unittest
import time
from user import User
from db import Db

class TestDb(unittest.TestCase):
    def setUp(self):
        self.db = Db("mongodb://localhost:27017")
        self.db.collection.delete_many({})

    def test_set_user_and_get_user(self):
        user = User(name = "test_user", mail = "test.user@test.com")

        self.db.set_user(user)
        result = self.db.get_user()

        self.assertIsNotNone(result)
        self.assertEqual(result.name, user.name)
        self.assertEqual(result.mail, user.mail)