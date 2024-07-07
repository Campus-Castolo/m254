from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import CORS
from modules.auth import auth
from modules.verify import verify
from modules.task_creation import task_creation
from modules.task_deletion import task_deletion

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You should set a secret key for session management
CORS(app)

# Register the auth blueprint with the /api prefix
app.register_blueprint(auth, url_prefix='/api')
# Register the verify blueprint with the /verify prefix
app.register_blueprint(verify, url_prefix='/verify')
# Register the task_creation blueprint with the /task prefix
app.register_blueprint(task_creation, url_prefix='/task_creation')
# Register the task_deletion blueprint with the /task prefix
app.register_blueprint(task_deletion, url_prefix='/task_deletion')

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

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")
