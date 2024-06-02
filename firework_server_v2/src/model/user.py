from src.db import db, flask_bcrypt
import datetime
from src.model.blacklist import BlacklistToken
from src.config import key
import jwt
from typing import Union
from src.model.enums import userTypeEnum, statusEnum, sexEnum
from sqlalchemy import Enum


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    middleName = db.Column(db.String(255))
    userTypeActual = db.Column(Enum(userTypeEnum)) 
    statusActual = db.Column(Enum(statusEnum)) 
    email = db.Column(db.String(255), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(255), unique=True, nullable=False)
    sexActual = db.Column(Enum(sexEnum), nullable=False)
    country = db.Column(db.String(255))
    city = db.Column(db.String(255))
    blocked = db.Column(db.Boolean, nullable=False, default=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, unique=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    password_hash = db.Column(db.String(100))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    admin = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=1, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            res = jwt.encode(payload, key, algorithm="HS256")
            return res
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key, algorithms=["HS256"])
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return "Token blacklisted. Please log in again."
            else:
                return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    def __repr__(self):
        return "<User '{}'>".format(self.lastName)
