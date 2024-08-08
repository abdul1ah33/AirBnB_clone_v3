#!/usr/bin/python3
'''
create flask app and register the blueprint app_views to flask instance app
'''
from models import storage
from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)


if __name__ == "__main__":
	"""Main Function"""
	host = getenv('HBNB_API_HOST', '0.0.0.0')
	port = environ.get('HBNB_API_PORT', 5000)
	app.run(host=host, port=port, threaded=True)
