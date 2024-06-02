from src.db import db
from sqlalchemy import Enum
from src.model.enums import clientTypeEnum

class TestsType2Id(db.Model):
    """Tests relation Model for storing id to client type connection"""

    __tablename__ = "test2id"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    clientTypeActual = db.Column(Enum(clientTypeEnum), nullable=False)

    def __repr__(self):
        return "<Test2id '{}'>".format(self.name)
