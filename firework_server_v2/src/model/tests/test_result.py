from src.db import db
import datetime


class TestResult(db.Model):
    """Test Result Model for storing related details"""

    __tablename__ = "testResult"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.String(100),
                     db.ForeignKey('user.public_id'),
                     nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    startDate  = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    spendTime  = db.Column(db.Interval)
    total = db.Column(db.Integer)

    def __repr__(self):
        return "<Test Result '{}'>".format(self.public_id)
    