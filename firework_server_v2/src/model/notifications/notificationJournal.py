from src.db import db

class NotificationJournal(db.Model):
    """Notification Journal Model for storing related details"""

    __tablename__ = "notificationJournal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.String(100),
                     db.ForeignKey('user.public_id'),
                     nullable=False)
    test_id = db.Column(db.String(100),
                     db.ForeignKey('testsList.public_id'),
                     nullable=False)
    sendNextTime = db.Column(db.DateTime, nullable=False)
    testIsFinished = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return "<Notification Journal '{}'>".format(self.public_id)