import unittest
import jwt
import datetime
import uuid

from src.db import db
from src.model.user import User
from test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_encode_auth_token(self):
        user = User(
            public_id=str(uuid.uuid4()),
            email="test@test.com",
            firstName="Иван",
            lastName="Иванов",
            phoneNumber="8(999)999-99-99",
            password="test",
            sexActual="male",
            blocked=False,
            userTypeActual="client",
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User(
            public_id=str(uuid.uuid4()),
            email="test@test.com",
            firstName="Иван",
            lastName="Иванов",
            phoneNumber="8(999)999-99-99",
            password="test",
            sexActual="male",
            blocked=False,
            userTypeActual="client",
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)

    def test_decode_auth_token_v2(self):
        token = jwt.encode({"test": "test"}, "TEST", algorithm="HS256")
        dec = jwt.decode(token, "TEST", algorithms=["HS256"])


if __name__ == "__main__":
    unittest.main()
