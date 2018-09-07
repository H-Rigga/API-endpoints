from flask import Flask, jsonify, request, session
from app.users import User
from app.orders import Order


user_object = User()
order_object = Order()

app = Flask (__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route('/')
def home_route():
    response = jsonify({'greetings': 'Greetings and welcome to Fast-food-fast'})
    return response, 200


@app.route('/api/v1/auth/register', methods=['POST'])
def signup():
    if request.method == "POST":
        first_name = request.json['first name']
        last_name = request.json['last name']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']
        msg = user_object.create_user(first_name,last_name, email, password, confirm_password)

        if msg['msg'] == 'User created successfully.':
            return jsonify(msg), 201
        elif msg['msg'] == 'Account with Email already exists. Please log in.' or 'Passwords do not match. Try again.':
            return jsonify(msg), 403


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        password = request.json['password']
        session['email'] = request.json['email']
        msg = user_object.login_user(session['email'], password)

        if msg['msg'] == 'Successfully logged in!':
            return jsonify(msg), 200
        elif msg['msg'] == 'Wrong Password. Try again.' or 'You have no account,please sign up':
            return jsonify(msg), 401


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    if request.method == "POST":
        if 'email' in session:
            session.pop('email', None)
            return jsonify({"message": "Logout successful"}), 200


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    if request.method == "POST":
        email = request.json['email']
        new_password = request.json['new_password']
        confirm_new_password = request.json['confirm_new_password']

        msg = user_object.reset_password(email, new_password, confirm_new_password)

        return jsonify(msg), 200


@app.route('/v1/api/orders', methods=['POST'])
def new_order():
    if 'email' in session:
        if request.method == "POST":
            orderer = session['email']
            what_order = request.json['what_order']

            msg = order_object.new_order(orderer,what_order)

            if msg["message"] == "Order received successfully.":
                return jsonify(msg), 201
            return jsonify(msg), 403


@app.route('/v1/api/orders/<int:orderId>', methods=['PUT'])
def update_order(orderId):
    if session.get('email') is not None:
        if request.method == "PUT":

            msg = order_object.update_order(orderId)
            if msg['msg'] == 'Order completed.':
                return jsonify(msg), 200
            return jsonify(msg), 403


@app.route('/v1/api/orders/<int:orderId>', methods=['DELETE'])
def delete_order(orderId):
    if session.get('email') is not None:
        if request.method == "DELETE":
            orderer = session['email']
            msg = order_object.delete_order(orderId)
            return jsonify(msg), 200


@app.route('/v1/api/orders', methods=['GET'])
def get_orders():
    if session.get('email') is not None:
        if request.method == "GET":
            msg = order_object.get_all_orders()
            return jsonify(msg), 200


@app.route('/v1/api/orders/<int:orderId>', methods=['GET'])
def get_order_by_id(orderId):
    if session.get('email') is not None:
        if request.method == "GET":
            msg = order_object.get_order_by_id(orderId)
            return jsonify(msg), 200
