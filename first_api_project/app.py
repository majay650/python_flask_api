from flask import Flask, jsonify, request
import mysql.connector
from flask_jsonschema_validator import JSONSchemaValidator
from functools import wraps


app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == "ajay" and auth.password == 'password':
            return f(*args, **kwargs)
        return "credentials are incorrect"
    return decorated

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="ajay",
#   database= "testdb1"
# )
