# from app import db
# from datetime import datetime, date
# from model_booking import Booking


# class Tours(db.Model):
#     __tablename__ = 'tours'  
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(120), unique=True)
#     price = db.Column(db.String(10))
#     date = db.Column(db.String(10))
#     bookings = db.relationship ("Booking", backref= 'tour', lazy=True)

#     def __repr__(self):
#         return f'<User {self.name}>'

