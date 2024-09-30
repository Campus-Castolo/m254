from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error
import hashlib
import uuid
import datetime

auth = Blueprint('auth', __name__)

# Configuration for PyCamunda ExternalTaskWorker
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 1,
    "retryTimeout": 5000,
    "sleepSeconds": 30,
}

# Creates connection to database with credentials stored in cleartext for easier development
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

# Generate personal access token
def generate_token():
    return str(uuid.uuid4())

@auth.route('/register', methods=['POST'])
def register():
    """
    Register a new user and generate a personal access token.
    """
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Check if passwords match
    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match!', 'status': 'text-danger'}), 400

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_id = str(uuid.uuid4())
    access_token = generate_token()
    created_at = datetime.datetime.now()

    # Create a database connection
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (id, username, email, password) VALUES (%s, %s, %s, %s)",
                           (user_id, username, email, hashed_password))
            
            # Insert the personal access token into the database
            cursor.execute("INSERT INTO access_token (token_id, token, created_at, users_id) VALUES (%s, %s, %s, %s)",
                           (str(uuid.uuid4()), access_token, created_at, user_id))
            
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
    """
    Test the database connection.
    """
    connection = create_connection()
    if connection:
        return jsonify({'message': 'Database connection successful!'}), 200
    else:
        return jsonify({'message': 'Database connection failed!'}), 500

