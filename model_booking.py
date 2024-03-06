from app import db
from datetime import date, datetime

class Booking(db.Model):
    __tablename__ = 'Reservas'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120))
    date = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    # tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'))