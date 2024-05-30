from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import mysql.connector
from mysql.connector import Error
import hashlib
import uuid

auth = Blueprint('auth', __name__)


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='testdatabase',
            user='testaccount',
            password='abcd12s8rkds',
            port=3306
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

@auth.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match!', 'status': 'text-danger'}), 400

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_id = str(uuid.uuid4())

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (id, username, email, password) VALUES (%s, %s, %s, %s)",
                           (user_id, username, email, hashed_password))
            connection.commit()
            return jsonify({'message': 'Registration successful!', 'status': 'text-success'}), 201
        except Error as e:
            return jsonify({'message': f"Error: {str(e)}", 'status': 'text-danger'}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({'message': 'Database connection failed!', 'status': 'text-danger'}), 500

@auth.route('/test-db-connection', methods=['GET'])
def test_db_connection():
    connection = create_connection()
    if connection:
        return jsonify({'message': 'Database connection successful!'}), 200
    else:
        return jsonify({'message': 'Database connection failed!'}), 500
