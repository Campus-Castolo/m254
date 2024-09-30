from flask import Flask, render_template, request, make_response
from flask_cors import CORS
from modules.auth import auth
from modules.verify import verify
import pycamunda.processinst



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

@app.route('/start-account-creation', methods=['POST'])
def start_account_creation():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    start_instance = pycamunda.processinst.StartInstance(
        url='http://localhost:8080/engine-rest',
        key='accountcreation',
        variables={
            'name': {'value': name, 'type': 'String'},
            'email': {'value': email, 'type': 'String'},
            'password': {'value': password, 'type': 'String'}
        }
    )
    try:
        response = start_instance()
        return jsonify({'message': 'Process started successfully!', 'data': response}), 200
    except pycamunda.PyCamundaException as e:
        return jsonify({'message': str(e)}), 500

@app.route('/start-email-verification', methods=['POST'])
def start_email_verification():
    email_token = request.form['email_token']
    email = request.form['email']

    start_instance = pycamunda.processinst.StartInstance(
        url='http://localhost:8080/engine-rest',
        key='email_verify',
        variables={
            'email_token': {'value': email_token, 'type': 'String'},
            'email': {'value': email, 'type': 'String'}
        }
    )
    try:
        response = start_instance()
        return jsonify({'message': 'Process started successfully!', 'data': response}), 200
    except pycamunda.PyCamundaException as e:
        return jsonify({'message': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")
