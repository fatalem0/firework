from src.db import db
import datetime


class TestLog(db.Model):
    """Test Log Model for storing related details"""

    __tablename__ = "testLog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.String(100),
                     db.ForeignKey('user.public_id'),
                     nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    testAnswersNumbers = db.Column(db.String(100))
    gettedScore = db.Column(db.Integer)
    dateStart = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    dateEnd = db.Column(db.DateTime)
    questionNumber = db.Column(db.BigInteger)


    def __repr__(self):
        return "<Test Log '{}'>".format(self.public_id)