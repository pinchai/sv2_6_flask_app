from flask import Flask, render_template
from  product import product

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('front/home.html')

@app.get('/product')
def product():
    return "product page"


@app.get('/product-detail')
def product_detail():
    return "product detail page"


@app.get('/cart')
def cart():
    return "cart page"


@app.get('/checkout')
def checkout():
    return "checkout page"


if __name__ == '__main__':
    app.run()
