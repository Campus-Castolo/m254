from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import CORS
from modules.auth import auth
from modules.verify import verify
from modules.task import create_task, delete_task

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You should set a secret key for session management
CORS(app)

# Register the auth blueprint with the /api prefix
app.register_blueprint(auth, url_prefix='/api')
# Register the verify blueprint with the /verify prefix
app.register_blueprint(verify, url_prefix='/verify')

@app.route("/")
def index():
    theme = request.cookies.get('theme', 'light')
    response = make_response(render_template('index.html', theme=theme))
    return response

@app.route('/verify')
def verify_page():
    return render_template('verify.html')

@app.route('/set_theme/<theme>')
def set_theme(theme):
    response = make_response('', 204)  # No content response
    response.set_cookie('theme', theme, max_age=30*24*60*60)  # Cookie expires in 30 days
    return response

@app.route('/clear_cookies')
def clear_cookies():
    response = make_response('', 204)  # No content response
    response.set_cookie('theme', '', expires=0)  # Expire the cookie immediately
    return response

@app.route('/create_task', methods=['POST'])
def create_task_endpoint():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_date = data.get('start_date')
    assign_user = data.get('assign_user')
    created_by = data.get('created_by')
    priority_id = data.get('priority_id')

    if not all([name, description, start_date, assign_user, created_by, priority_id]):
        return jsonify({'message': 'All fields are required.'}), 400

    try:
        create_task(name, description, start_date, assign_user, created_by, priority_id)
        return jsonify({'message': 'Task created successfully.'}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@app.route('/delete_task', methods=['POST'])
def delete_task_endpoint():
    data = request.get_json()
    task_id = data.get('id')

    if not task_id:
        return jsonify({'message': 'Task ID is required.'}), 400

    try:
        delete_task(task_id)
        return jsonify({'message': 'Task deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")
