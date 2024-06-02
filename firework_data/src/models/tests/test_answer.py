from src.db import db


class TestAnswer(db.Model):
    """Test Answer Model for storing related details"""

    __tablename__ = "testAnswer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    test_question_id = db.Column(db.String(100),
                     db.ForeignKey('testQuestion.public_id'),
                     nullable=False)
    answerNumber = db.Column(db.Integer)
    score = db.Column(db.Integer)
    answerText = db.Column(db.String(100))

    def __repr__(self):
        return "<Test Answer '{}'>".format(self.public_id)
