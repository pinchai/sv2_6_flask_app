from flask import Flask, render_template, request, make_response
from product import get_product_by_id, get_product_by_category, products as pr
import json

app = Flask(__name__)


@app.get('/')
@app.get('/home')
def home():
    return render_template('front/index.html', products=pr)


@app.get('/products')
def products():
    return render_template(
        'front/products.html',
        products=pr
    )


@app.get('/product/<int:product_id>')
def product(product_id):
    product = get_product_by_id(product_id)
    related_product = get_product_by_category(product['category'])
    return render_template(
        'front/product.html',
        product=product,
        related_product=related_product
    )


@app.get('/cart')
def cart():
    product_id = request.args.get('product_id')
    cart_list = request.cookies.get('cart_list')
    cart_list = json.loads(cart_list) if cart_list else []
    if product_id:
        duplicate_product_ids = [item['id'] for item in cart_list]
        if product_id in duplicate_product_ids:
            for item in cart_list:
                if item['id'] == product_id:
                    item['qty'] += 1
        else:
            cart_list.append({"id": product_id, "qty": 1})
    elif not product_id or product_id == '':
        pass
    # map data
    for item in cart_list:
        # assert False, get_product_by_id(12)['image']
        item['image'] = get_product_by_id(item['id'])['image']
        item['title'] = get_product_by_id(item['id'])['title']
        item['price'] = get_product_by_id(item['id'])['price']
        item['category'] = get_product_by_id(item['id'])['category']
        item['description'] = get_product_by_id(item['id'])['description']
    response = make_response(render_template('front/cart.html', cart_list=cart_list))
    response.set_cookie('cart_list', json.dumps(cart_list))
    return response


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


@app.get('/admin/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('admin/dashboard/dashboard.html', module=module)

@app.get('/admin/user')
def user():
    module = 'user'
    return render_template('admin/user/user.html', module=module)



if __name__ == '__main__':
    app.run()
