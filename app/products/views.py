from app.__init__ import db
from flask import render_template, request, redirect, url_for
from app.products import product_blueprint
from flask import Blueprint
from app.models import Product

# product_blueprint = Blueprint('product', __name__, url_prefix='/products')


@product_blueprint.route('/', endpoint='product_home')
def home():
    products = Product.get_all_objects()
    return render_template('products/home.html', products=products)

@product_blueprint.route('/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        image = request.form.get('image')
        section = request.form.get('section')

        product = Product(name=name, image=image, section=section)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('products.product_home'))

    return render_template('products/create_product.html')





@product_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.image = request.form.get('image')
        product.section = request.form.get('section')
        product.description = request.form.get('description')  # Update the description
        db.session.commit()

        return redirect(url_for('products.product_home'))

    return render_template('products/edit_product.html', product=product)



@product_blueprint.route('/details/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)

    return render_template('products/details.html', product=product)



@product_blueprint.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.product_home'))
