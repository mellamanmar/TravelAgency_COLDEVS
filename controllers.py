from flask import request, jsonify
from models import Tour as Tours, Booking, User 
from app import db
from serializers import TourSchemaPost, TourSchemaGet, TourSchemaShow, TourSchemaPut

#Tours

def post_tour():
    tour_data_schema = TourSchemaPost()
    data = request.json
    
    try:
        tour_data_schema.load(data)
    except ValidationError as err:

        return jsonify({'error': err.messages}), 400

    new_tour = Tours(
        name = data['name'],
        description = data['description'],
        price = data['price'],
        date = data['date']
    )
    db.session.add(new_tour)
    db.session.commit()
    return ({'response': 'Tour successfully created'}), 201
    

def get_tour():
    tour_schema = TourSchemaGet()
    tours = Tours.query.all()
    return jsonify([tour_schema.dump(tour) for tour in tours])


def show_tour(tour_id):
    tour_schema = TourSchemaShow()
    tour = Tours.query.get_or_404(tour_id)
    return jsonify(tour_schema.dump(tour))


def put_tour(tour_id):
    tour_data_schema = TourSchemaPut()
    data = request.json
    
    try:
        tour_data_schema.load(data)
    except ValidationError as err:

        return jsonify({'error': err.messages}), 400
    
    tour = Tours.query.get_or_404(tour_id)
    data = request.get_json()
    tour.name = data['name']
    tour.description = data['description']
    tour.price = data['price']
    tour.date = date['date']
    db.session.commit()
    return jsonify({'response': 'Tour successfully updated'})


def delete_tour(tour_id):
    tour = Tours.query.get_or_404(tour_id)
    db.session.delete(tour)
    db.session.commit()
    return jsonify({'response': 'Tour successfully deleted'})


#Bookings

from serializers import BookingSchemaPost, BookingSchemaGet, BookingSchemaShow

def post_booking():
    booking_data_schema = BookingSchemaPost()
    data = request.json
    
    try:
        booking_data_schema.load(data)
    except ValidationError as err:

        return jsonify({'error': err.messages}), 400

    data = request.get_json()
    new_booking = Booking(
    quantity=data['quantity'], 
    date=data['date'],
    user_id=data['user_id'],
    tour_id=data['tour_id']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'response': 'Booking successfully created'}), 201

def get():
    booking_schema = BookingSchemaGet()
    bookings = Booking.query.all()
    return jsonify([booking_schema.dump(booking) for booking in bookings])

def show_by_user(user):
    user = int(user)
    booking_schema = BookingSchemaShow()
    bookings = Booking.query.filter_by(user_id=user).all()
    return jsonify([booking_schema.dump(booking) for booking in bookings])

def delete_booking(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    return jsonify({'response': 'Booking successfully deleted'})

# User

from serializers import UserSchemaPost

def create_user():
    user_data_schema = UserSchemaPost()
    data = request.json
    
    try:
        user_data_schema.load(data)
    except ValidationError as err:

        return jsonify({'error': err.messages}), 400
    data = request.get_json()
    new_user = User(user=data['user'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'response': 'User successfully created'}), 201