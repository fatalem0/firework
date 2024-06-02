from src.db import db, flask_bcrypt
import datetime
from src.models.enums import userTypeEnum, statusEnum, sexEnum
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