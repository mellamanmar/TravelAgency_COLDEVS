from app import db
from datetime import datetime, date
from booking import Booking


class Tours(db.Model):
    my_str_date = '24-09-2023'
    __tablename__ = 'Tours'  
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120), unique=True)
    price = db.Column(db.String(10))
    date = db.Column(db.String(10))
    # bookings = db.relationship ("Booking", backref= 'tour')

    def __repr__(self):
        return f'<User {self.name}>'

