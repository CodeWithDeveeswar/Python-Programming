# Run product_api.py and use curl command

from flask import Flask, request, jsonify

app = Flask(__name__)

cart = []

@app.route('/')
def index():
    return jsonify(cart)

@app.route('/api/add', methods=['POST'])
def add_to_cart():
    product_name = request.form.get('name')
    if not product_name:
        return jsonify({'error': 'Product name is required'}), 400

    product = {'name': product_name}
    cart.append(product)
    return jsonify({'message': 'Product added to cart', 'cart': cart}), 201

@app.route('/api/delete/<string:product_name>', methods=['DELETE'])
def delete_from_cart(product_name):
    global cart
    initial_length = len(cart)
    cart = [product for product in cart if product['name'] != product_name]

    if len(cart) < initial_length:
        return jsonify({'message': 'Product removed from cart', 'cart': cart}), 200
    else:
        return jsonify({'error': 'Product not found in cart'}), 404

if __name__ == '__main__':
    app.run(debug=True)
