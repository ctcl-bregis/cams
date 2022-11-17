# Import "db" from the main script (app.py)
from app import db

class memd(db.Model):
    __tablename__ = "artists"
    
    inid = db.Column(db.Integer, primary_key = True)
    note = db.Column(db.Integer)
