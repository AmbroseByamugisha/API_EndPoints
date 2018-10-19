from flask import Flask, json, request, jsonify
app = Flask(__name__)

# all my products static data
products = [
    {
        "product_id": 1,
        "name": "paper",
        "quantity": "10",
        "quality":"good"
    },
    {  
        "product_id": 2,
        "name": "bags",
        "quantity": "5",
        "quality": "poor"
    },
    {
        "product_id": 3,
        "name": "shirts",
        "quantity": "100",
        "quality": "excellent"
    }
]

# all sales records
sales = [
    {
        "sale_id": 1,
        "item": "paper",
        "amount": "1000"
    },
    {
        "sale_id": 2,
        "item": "computer",
        "amount": "400"
    },
    {
        "sale_id": 3,
        "item": "tables",
        "amount": "340"
    }
]

# home page
@app.route('/', methods=['GET'])
def home():
    return jsonify('This is Home Page')

# admin/store attendant can get all products
@app.route('/todo/api/v1/products', methods=['GET'])
def get_all_products():
    prod = []
    for product in products:
        prod.append(product)
    return jsonify ({'products': prod}) 
 
# admin/store attendant can get a specific product
@app.route('/todo/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product["product_id"] == product_id]
    return jsonify({'product': product[0]})

# admin can add a new product
@app.route('/todo/api/v1/products', methods=['POST'])
def add_product():
    product = request.get_json()
    product_id = product['product_id']
    name = product['name']
    quantity = product['quantity']
    quality = product['quality']
    products.append(product)
    return jsonify(products)

# admin/store attendant can get all sales records
@app.route('/todo/api/v1/sales', methods=['GET'])
def get_all_sales():
    data = []
    for sale in sales:
        data.append(sale)
    return jsonify({'sales': data})

# admin/store attendant can fetch a single sale record
@app.route('/todo/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = [sale for sale in sales if sale["sale_id"] == sale_id]
    return jsonify({'sale': sale[0]})
    
# store attendant can create a sale order
@app.route('/todo/api/v1/sales', methods=['POST'])
def add_sale():
    sale = request.get_json()
    sale_id = sale['sale_id']
    item = sale['item']
    amount = sale['amount']
    sales.append(sale)
    return jsonify(sales)

if __name__ == '__main__':
    app.run(debug=True)