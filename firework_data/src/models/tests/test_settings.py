from src.db import db
from sqlalchemy import Enum
from src.models.enums import stressLevelEnum


class TestSettings(db.Model):
    """Test Settings Model for storing related details"""

    __tablename__ = "testSettings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    stressLevelActual = db.Column(Enum(stressLevelEnum), nullable=False)
    minCount = db.Column(db.Integer)
    maxCount = db.Column(db.Integer)
    description = db.Column(db.String(100))
    recommendation = db.Column(db.String(100))

    def __repr__(self):
        return "<Tests Setting '{}'>".format(self.public_id)