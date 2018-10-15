from flask import Flask, json, request
app = Flask(__name__)

# all my products static data
products = [
    {
        "name": "paper",
        "quantity": "10",
        "quality":"good"
    },
    {
        "name": "bags",
        "quantity": "5",
        "quality": "poor"
    },
    {
        "name": "shirts",
        "quantity": "100",
        "quality": "excellent"
    }
]

# Hello world
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
# trial 1
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# admin/store attendant can get all products
@app.route('/products', methods=['GET'])
def products():
    return '<h1>my products are</h1> ' + json.dumps([{"name": "paper", "qty": "6", "desc": "good"}])
    #return json.dumps(products)
    # how to get my static data
    # test my single route

# admin/store attendant can get a specific product
@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    return '<h1>my product is</h1> %d' % id

# admin can get all sales records
# specify roles with admin
# use Boolean
@app.route('/sales', methods=['GET'])
def sales():
    return '<h1>Sales</h1> ' + json.dumps([{"sales_id": "1", "items": "soap", "desc": "good"}])

# admin can add a product
# need to add roles and apply Boolean logic
# like is _admin = True or False
@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        return 'Product successfully added.'
    else:
        return 'Nothing done.'
    
# store attendant can add a sale order
@app.route('/add_sale', methods=['POST'])
def add_sale():
    if request.method == 'POST':
        return 'Sale Order successfully added.'
    else:
        return 'Sales order failed.'

if __name__ == '__main__':
    app.run(debug=True)