import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/neworders', methods=['GET'])
def fetch_all_orders():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from products")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/add', methods=['POST'])
def add_order():
    try:
        json = request.json
        name = json['name']
        model = json['model']
        quantity = json['quantity']
        # validate the received values
        if name and model and quantity and request.method == 'POST':
            sql = "INSERT INTO products(name, model, quantity) VALUES(%s, %s, %s)"
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

@app.route('/neworders/update', methods = ['PUT'])
def update_order():
    try:
        json = request.json
        id = json['id']
        name = json['name']
        model = json['model']
        quantity = json['quantity']
        # validate the received values
        if name and model and quantity and id and request.method == 'PUT':
            sql = "UPDATE products SET name=%s, model=%s, quantity=%s WHERE id=%s"
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


if __name__ == "__main__":
    app.run()