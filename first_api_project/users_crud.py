import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from app_errors import *
from orders_crud import *
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/users', methods = ['GET'])
def fetch_all_users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users/add', methods = ['POST'])
def add_user():
    try:
        json = request.json
        first_name = json['first_name']
        last_name = json['last_name']
        email = json['email']
        password = json['password']
        address = json['address']
        if first_name and last_name and email and password and address and request.method == 'POST':
            hashed = generate_password_hash(password)
            sql_formula= 'INSERT INTO users (first_name, last_name, email_address, password, address) VALUES (%s, %s, %s, %s, %s)'
            data = (first_name, last_name, email, hashed, address)
            # return jsonify(data)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql_formula, data)
            conn.commit()
            resp = jsonify("User added successfully")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)







if __name__ == "__main__":
    app.run(debug=True)

