#!/usr/bin/python3
"""index"""
form flask import jsonify
from api.v1.views import app_views

@app_views_route('/status')
def api_status():
""" Status of API """
response = {"status": "OK"}
return jsonify(response)
