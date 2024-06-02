from flask_testing import TestCase

from src.db import db
from app import app


class BaseTestCase(TestCase):
    """Base Tests"""

    def create_app(self):
        app.config.from_object("src.config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
