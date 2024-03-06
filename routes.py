from flask import request, jsonify, Blueprint
from app import db

# Users

from controllers import create_user

user_r = Blueprint('user_r', __name__)

@user_r.route('/user', methods=['POST'])
def post_user():
    return create_user()
    
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

@booking_r.route('/booking/<user>', methods=['GET'])
def list_booking(user):
    return show_by_user(user)

@booking_r.route('/booking/<booking_id>', methods=['DELETE'])
def delete_booking_by_id(booking_id):
    return delete_booking(booking_id)