from app import create_app, db
from models import Tour, Booking, User


app = create_app()

with app.app_context():
    Tour.__table__.create(db.engine)
    User.__table__.create(db.engine)
    Booking.__table__.create(db.engine)