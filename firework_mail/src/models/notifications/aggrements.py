from src.db import db

class Aggrements(db.Model):
    """Aggrement Model for storing clients notification aggrement"""

    __tablename__ = "aggrement"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.String(100),
                     db.ForeignKey('user.public_id'),
                     nullable=False,
                     unique=True)
    hasTGAggrement = db.Column(db.Boolean, nullable=False)
    hasMailAggrement = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return "<Aggrement '{}'>".format(self.public_id)
