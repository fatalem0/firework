from src.db import db
from sqlalchemy import Enum
from src.model.enums import clientTypeEnum, stagesEnum

class TestsList(db.Model):
    """Tests List Model for storing related details"""

    __tablename__ = "testsList"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100))
    stageActual = db.Column(Enum(stagesEnum), nullable=False)
    interval = db.Column(db.Integer)
    numberOfQuestions  = db.Column(db.Integer)

    def __repr__(self):
        return "<Tests List '{}'>".format(self.name)
