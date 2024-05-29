from flask import Blueprint, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
import hashlib
import uuid

auth = Blueprint('auth', __name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

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

@auth.route('/')
def index():
    return render_template('index.html')
