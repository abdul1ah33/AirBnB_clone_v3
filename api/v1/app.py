#!/usr/bin/python3
""" Flask Application """
from os import getenv
from models import storage
from flask import Flask, jsonify, make_response
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"api/v1/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = getenv('HBNB_API_PORT', 5000)
    app.run(host=HOST, port=PORT, threaded=True)
