from src.db import db
from src.models.enums import chanelTypeEnum, sendingStatusEnum
from sqlalchemy import Enum


class NotificationLog(db.Model):
    """Notification Log Model for storing related details"""

    __tablename__ = "notificationLog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100),
                     db.ForeignKey('user.email'),
                     nullable=False)
    chanel = db.Column(Enum(chanelTypeEnum), nullable=False)
    tgChatId = db.Column(db.String(100))
    status = db.Column(Enum(sendingStatusEnum), nullable=False)
    sendTime = db.Column(db.DateTime, nullable=False)
    errorDescription = db.Column(db.String())


    def __repr__(self):
        return "<Notification Log '{}'>".format(self.public_id)