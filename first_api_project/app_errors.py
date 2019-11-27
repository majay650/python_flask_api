from app import app
from flask import jsonify

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'The api url is not correct'
    }
    resp = jsonify(message)
    return resp

@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': 500,
        'message': 'There is problem with server. Server is not responding'
    }
    resp = jsonify(message)
    return resp