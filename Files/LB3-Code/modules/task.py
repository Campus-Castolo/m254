from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

task = Blueprint('task', __name__)