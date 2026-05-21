from flask import Flask, render_template
from product import  products as pr

app = Flask(__name__)


@app.get('/')
@app.get('/home')
def home():
    return render_template('front/index.html', products=pr)


@app.get('/products')
def products():
    return render_template('front/products.html', products=pr)


@app.get('/product/<product_id>')
def product(product_id):
    return render_template('front/product.html')


@app.get('/cart')
def cart():
    return render_template('front/cart.html')


@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')


@app.get('/account')
def account():
    return render_template('front/account.html')


@app.get('/forgot-password')
def forgot_password():
    return render_template('front/forgot-password.html')


@app.get('/login')
def login():
    return render_template('front/login.html')


@app.get('/create-user')
def create_user():
    return render_template('front/create-user.html')


if __name__ == '__main__':
    app.run()
