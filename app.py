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
    return json.dumps([{"name": "paper", "qty": "6", "desc": "good"}])
    #return json.dumps(products)
    # how to get my static data
    # test my single route

# admin/store attendant can get a specific product
@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    return 'my product is %d' % id



if __name__ == '__main__':
    app.run(debug=True)