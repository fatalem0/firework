from src.db import db
from src.model.enums import cureTypeEnum
from sqlalchemy import Enum

class ClientsCure(db.Model):
    """Clients Cure Model for storing clients cure types"""

    __tablename__ = "clients_cure"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    public_client_id = db.Column(db.String(100),
                     db.ForeignKey('client.public_id'),
                     nullable=False)
    cureType = db.Column(Enum(cureTypeEnum), nullable=False)
    
    def __repr__(self):
        return "<Cure '{}'>".format(self.public_id)