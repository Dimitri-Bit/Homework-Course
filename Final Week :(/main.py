from flask import Flask, request
from database import database_manager
import json

database_m = database_manager()
app = Flask(__name__)

@app.route("/")
def home():
    return "Dobrodosli!"

@app.route("/register", methods=["POST"])
def register():
    request_data = request.get_json()
    username = request_data['username']
    email = request_data['email']
    password = request_data['password']

    success = database_m.register_user(username, email, password, '')
    if not success:
        return json.dumps({"error": "User already exists"}), 401
    else:
        return json.dumps({"message": "User created"}), 201
    
@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    result = database_m.login_user(username, password)

    if result == "Correct Password":
        return json.dumps({"error": "Logged in"}), 200
    elif result == "Incorrect Password":
        return json.dumps({"error": "Incorrect Password"}), 401
    else:
        return json.dumps({"error": "User does not exist"}), 404


if __name__ == "__main__":
    app.run(port=8080, debug=True)