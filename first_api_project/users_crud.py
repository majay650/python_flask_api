import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from app_errors import *
from orders_crud import *
from app import auth_required
from db_config import conn
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jsonschema_validator import JSONSchemaValidator
from functools import wraps


@app.route('/users', methods = ['GET'])
@auth_required
def fetch_all_users():
    try:
        # conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()

@app.route('/users/add', methods = ['POST'])
@auth_required
def add_user():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    password = request.json.get('password') or 'password'
    address = request.json.get('address')
    if request.method== 'POST':
        if not 'first_name' in request.json or not request.json.get('first_name'):
            return jsonify(message="First name and email is mandatory")
        if not 'email' in request.json or not request.json.get('email'):
            return jsonify(message="First name and email is mandatory")
        sql_formula = 'INSERT INTO users (first_name, last_name, email_address, password, address) VALUES (%s, %s, %s, %s, %s)'
        data = (first_name, last_name, email, password, address)
        cursor = conn.cursor()
        cursor.execute(sql_formula, data)
        conn.commit()
        resp = jsonify('User added successfully')
        resp.status_code = 200
        return resp

if __name__ == "__main__":
    app.run(debug=True)

