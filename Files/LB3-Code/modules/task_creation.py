from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

task_creation = Blueprint('task_creation', __name__)

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

@task_creation.route('/create_task', methods=['POST'])
def create_task():
    data = request.form
    name = data.get('name')
    priority_id = data.get('priority_id')

    connection = create_connection()
    if connection is None:
        return jsonify({'message': 'Error connecting to the database'}), 500

    try:
        cursor = connection.cursor()
        sql_insert_task = """INSERT INTO task (name, priority_id) VALUES (%s, %s)"""
        cursor.execute(sql_insert_task, (name, priority_id))
        connection.commit()
        return jsonify({'message': f"Task '{name}' created successfully."})
    except Error as e:
        return jsonify({'message': f"Error while creating task: {e}"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
