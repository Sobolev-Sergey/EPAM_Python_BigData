from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

app = Flask(__name__)


ORDERS = [
    {
        'id': 1,
        'name': 'Book',
        'price': 5000
    }
]


@app.route('/')
def hello():
    return {
        'text': 'text'
    }


@app.route('/api/orders/', methods=['GET'])
def orders():
    return jsonify(ORDERS)


@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    orders = [order for order in ORDERS if order['id'] == order_id]
    return jsonify(orders)


@app.route('/api/orders/', methods=['POST'])
def create_order():
    print(request.json)

    if 'name' in request.json and 'price' in request.json:
        new_order = {
            'id': ORDERS[-1]['id'] + 1,
            'name': request.json['name'],
            'price': request.json['price']
        }
        ORDERS.append(new_order)

        return new_order, 201
    else:
        abort(400)


@app.route('/api/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    return 501


@app.route('/api/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    return 501
