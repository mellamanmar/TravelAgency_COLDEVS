from flask import request, jsonify
from tour import Tours
from booking import Booking
from app import db


#Tours

def post_tour():

    request_form = request.get_json()
    new_tour = Tours(
        name = request_form['name'],
        description = request_form['description'],
        price = request_form['price'],
        date = request_form['date']
    )
    db.session.add(new_tour)
    db.session.commit()
    return ({'response': 'Tour successfully created'}), 201
    

def get_tour():
    tours = Tours.query.all()
    return jsonify([{'id': tour.id, 'name': tour.name, 'description': tour.description, 
    'price': tour.price, 'date': tour.date } for tour in tours])


def show_tour(tour_id):
    tour = Tours.query.get_or_404(tour_id)
    return jsonify({'id': tour.id, 'name': tour.name, 'description': tour.description, 
    'price': tour.price, 'date': tour.date})


def put_tour(tour_id):
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

def post_booking():
    data = request.get_json()
    new_booking = Booking(
    user=data['user'], 
    quantity=data['quantity'], 
    date=data['date']
    # tour_id=data['tour_id']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'response': 'Booking successfully created'}), 201


def get():
    bookings = Booking.query.all()
    return jsonify([{'id': booking.id, 'user': booking.user, 'quantity': booking.quantity, 
    'date': booking.date} for booking in bookings])


def show_by_user(user):
    booking_user = request.args.get(user)
    if not user:
        booking_user = Booking.query.all()
        return jsonify([{'id': booking.id, 'user': booking.user, 
        'quantity': booking.quantity, 'date': booking.date} for booking in bookings])
    else:
        booking_user = session.query(Booking).filter(Booking.user == user)
    return jsonify({'id': booking.id, 'user': booking.user, 'quantity': booking.quantity})


def delete_booking(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    return jsonify({'response': 'Booking successfully deleted'})