from src.db import db
from sqlalchemy import Enum
from src.model.enums import questionTypeEnum


class TestQuestion(db.Model):
    """Test Question Model for storing related details"""

    __tablename__ = "testQuestion"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    questionNumber = db.Column(db.BigInteger)
    title = db.Column(db.String(200))
    questionTypeActual = db.Column(Enum(questionTypeEnum), nullable=False)

    def __repr__(self):
        return "<Test Question '{}'>".format(self.public_id)
    