from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    theme = request.cookies.get('theme', 'light')
    response = make_response(render_template('index.html', theme=theme))
    return response

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
    app.run(debug=True, port="5000", host="localhost")