from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

verify = Blueprint('verify', __name__)

# creates connection to database with credentials stored in cleartext for easier development
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

@verify.route('/verify', methods=['POST'])
def verify_account():
    """
    Verify user's account with personal access token.
    """
    token = request.form.get('token')

    # Create a database connection
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Check if the token exists in the database
            cursor.execute("SELECT * FROM access_token WHERE token = %s", (token,))
            token_data = cursor.fetchone()
            if token_data:
                user_id = token_data[3]  # Get the user ID associated with the token
                # Update the user's account status to verified
                cursor.execute("UPDATE users SET verified = 1 WHERE id = %s", (user_id,))
                connection.commit()
                return jsonify({'message': 'Account verified successfully!', 'status': 'text-success'}), 200
            else:
                return jsonify({'message': 'Invalid token!', 'status': 'text-danger'}), 400
        except Error as e:
            return jsonify({'message': f"Error: {str(e)}", 'status': 'text-danger'}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({'message': 'Database connection failed!', 'status': 'text-danger'}), 500
