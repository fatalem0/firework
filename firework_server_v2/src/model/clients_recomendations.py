from src.db import db
from src.model.enums import recomendationTypeEnum
from sqlalchemy import Enum

class ClientsRecomendations(db.Model):
    """Clients Recomendations Model for storing clients recomendations"""

    __tablename__ = "clients_recomendation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    public_client_id = db.Column(db.String(100),
                     db.ForeignKey('client.public_id'),
                     nullable=False)
    recomendationType = db.Column(Enum(recomendationTypeEnum), nullable=False)
    recomendationDescription = db.Column(db.String(250))
    
    def __repr__(self):
        return "<Recomendation '{}'>".format(self.public_id)