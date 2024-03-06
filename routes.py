from flask import request, jsonify, Blueprint
from app import db
from user import User
from tour import Tours
from booking import Booking
from datetime import datetime, date



main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def post():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'response': 'User successfully created'}), 201

@main.route('/users', methods=['GET'])
def get():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@main.route('/users/<id>', methods=['GET'])
def show(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

@main.route('/users/<id>', methods=['PUT'])
def put(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'response': 'User successfully updated'})

@main.route('/users/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'response': 'User successfully deleted'})

#Tours

from controllers import post_tour, get_tour, show_tour, put_tour, delete_tour

tours_r = Blueprint('tours_r', __name__)

@tours_r.route('/tour', methods= ['POST', 'GET'])
def list_create_tour():
    if request.method == 'POST': return post_tour()
    if request.method == 'GET': return get_tour()

    else: return 'Method is Not Allowed'

@tours_r.route("/tour/<tour_id>", methods= ['GET', 'PUT', 'DELETE'])
def show_update_delete_tour(tour_id):
    if request.method == 'GET': return show_tour(tour_id)
    if request.method == 'PUT': return put_tour(tour_id)
    if request.method == 'DELETE': return delete_tour(tour_id)

from controllers import delete_booking, post_booking, show_by_user

#Booking
booking_r = Blueprint('booking_r', __name__)

@booking_r.route('/booking', methods=['POST'])
def create_booking():
    if request.method == 'POST': return post_booking()

@booking_r.route('/booking/<booking_user>', methods=['GET'])
def list_booking(booking_user):
    if request.method == 'GET': return show_by_user(booking_user)

@booking_r.route('/booking/<booking_id>', methods=['DELETE'])
def delete_booking_by_id(booking_id):
    return delete_booking(booking_id)