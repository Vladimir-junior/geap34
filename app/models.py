from sqlalchemy.dialects.postgresql import JSONB

from app import db

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)
    area = db.Column(JSONB)