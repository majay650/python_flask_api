from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="ajay",
#   database= "testdb1"
# )
