from app import db

class Tour(db.Model):
    __tablename__ = 'tours'  
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120), unique=True)
    price = db.Column(db.String(10))
    date = db.Column(db.String(10))
    bookings = db.relationship ("Booking", backref= 'tour', lazy=True)

    def __repr__(self):
        return f'<Tour {self.name}>'

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    bookings = db.relationship("Booking", backref= 'user', lazy=True)

    def __repr__(self):
        return f'<User {self.user}>'

class Booking(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=True)