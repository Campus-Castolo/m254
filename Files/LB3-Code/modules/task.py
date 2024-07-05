from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

task = Blueprint('task', __name__)

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

def create_task(name, priority_id):
    connection = create_connection()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        sql_insert_task = """INSERT INTO task (name, priority_id) VALUES (%s, %s)"""
        cursor.execute(sql_insert_task, (name, priority_id))
        connection.commit()
        print(f"Task '{name}' created successfully.")
    except Error as e:
        print(f"Error while creating task: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_task(task_id):
    connection = create_connection()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        sql_delete_task = """DELETE FROM task WHERE id = %s"""
        cursor.execute(sql_delete_task, (task_id,))
        connection.commit()
        print(f"Task with ID {task_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting task: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
