import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from app_errors import *

@app.route('/orders', methods=['GET'])
def fetch_all_orders():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from orders")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/orders/add', methods=['POST'])
def add_order():
    try:
        json = request.json
        name = json['name']
        model = json['model']
        quantity = json['quantity']
        # validate the received values
        if name and model and quantity and request.method == 'POST':
            sql = "INSERT INTO orders(name, model, quantity) VALUES(%s, %s, %s)"
            data = (name, model, quantity,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Product added successfully!')
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/orders/update', methods = ['PUT'])
def update_order():
    try:
        json = request.json
        id = json['id']
        name = json['name']
        model = json['model']
        quantity = json['quantity']
        # validate the received values
        if name and model and quantity and id and request.method == 'PUT':
            sql = "UPDATE orders SET name=%s, model=%s, quantity=%s WHERE id=%s"
            data = (name, model, quantity, id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Product updated successfully!')
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/orders/<int:id>')
def fetch_single_order(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from orders WHERE id = %s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/orders/delete/<int:id>', methods=['DELETE'])
def delete_single_order(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE from orders WHERE id = %s", id)
        conn.commit()
        resp = jsonify ('Order deleted successfully')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/orders/deleteall/')
def delete_all_orders():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders")
        conn.commit()
        resp = jsonify("Orders deleted successfully")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

# @app.route('/users', methods = ['GET'])
# def fetch_all_users():
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT * from users")
#         rows = cursor.fetchall()
#         resp = jsonify(rows)
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#
if __name__ == "__main__":
    app.run(debug=True)

