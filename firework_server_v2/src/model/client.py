from src.db import db
from src.model.enums import clientTypeEnum, stagesEnum, experienceTypeEnum
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

class Client(db.Model):
    """Client Model for storing client related details"""

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    public_user_id = db.Column(db.String(100),
                     db.ForeignKey('user.public_id'),
                     nullable=False,
                     unique=True)
    clientEmail = db.Column(db.String(100),
                     db.ForeignKey('user.email'),
                     nullable=False,
                     unique=True)
    clientFullName = db.Column(db.String(100), nullable=False)
    clientCreated = db.Column(db.DateTime,
                     db.ForeignKey('user.created'),
                     nullable=False,
                     unique=True)
    clientTypeActual = db.Column(Enum(clientTypeEnum), nullable=False)
    diseaseLocation = db.Column(db.String(255))
    stageActual = db.Column(Enum(stagesEnum))
    monthsAfterTreatment = db.Column(db.String(255))
    workWithPsychologist = db.Column(db.Boolean)
    experienceTypeActual = db.Column(Enum(experienceTypeEnum))
    experienceDescription = db.Column(db.String(255))
    duration = db.Column(db.Float)
    
    def __repr__(self):
        return "<Client '{}'>".format(self.public_id)
