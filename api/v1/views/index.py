#!/usr/bin/python3
"""index"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def api_status():
    """ Status of API """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats')
def api_stats():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
