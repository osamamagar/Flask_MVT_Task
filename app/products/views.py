from app.__init__ import db
from flask import render_template, request, redirect, url_for
from app.products import product_blueprint
# from flask import Blueprint
from app.models import Product, Section
#
# product_blueprint = Blueprint('product', __name__, url_prefix='/products')
#
#
# @product_blueprint.route('/', endpoint='product_home')
# def home():
#     products = Product.get_all_objects()
#     return render_template('products/home.html', products=products)
#
# @product_blueprint.route('/create', methods=['GET', 'POST'])
# def create_product():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         image = request.form.get('image')
#         section = request.form.get('section')
#
#
#         product = Product(name=name, image=image, section=section)
#         db.session.add(product)
#         db.session.commit()
#
#         return redirect(url_for('products.product_home'))
#
#     return render_template('products/create_product.html')
#
#
#
#
#
# @product_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
# # def edit_product(id):
# #     product = Product.query.get_or_404(id)
# #
# #     if request.method == 'POST':
# #         product.name = request.form.get('name')
# #         product.image = request.form.get('image')
# #         product.section = request.form.get('section')
# #         product.description = request.form.get('description')  # Update the description
# #         db.session.commit()
# #
# #         return redirect(url_for('products.product_home'))
# #
# #     return render_template('products/edit_product.html', product=product)
# #
#
#
# @product_blueprint.route('/details/<int:product_id>')
# def product_details(product_id):
#     product = Product.query.get_or_404(product_id)
#
#     return render_template('products/details.html', product=product)
#
#
#
# @product_blueprint.route('/delete/<int:product_id>', methods=['POST'])
# def delete_product(product_id):
#     product = Product.query.get_or_404(product_id)
#     db.session.delete(product)
#     db.session.commit()
#     return redirect(url_for('products.product_home'))


@product_blueprint.route('/', endpoint='product_home')
def product_home():
    products = Product.query.all()
    return render_template('products/product_home.html', products=products)



@product_blueprint.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        section_id = request.form['section_id']

        # Access the image file from request.files
        if 'image' in request.files:
            image = request.files['image']
            # Process the image as needed, e.g., save it to a folder or database.

            product = Product(name=name, image=image.filename, description=description, section_id=section_id)
            db.session.add(product)
            db.session.commit()

            return redirect(url_for('products.product_home'))
        else:
            return "No image file provided in the request."

    sections = Section.query.all()
    return render_template('products/create_product.html', sections=sections)


@product_blueprint.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    products = Product.query.get(product_id)
    if request.method == 'POST':
        products.name = request.form['name']
        products.image = request.form['image']
        products.description = request.form['description']
        products.section_id = request.form['section_id']

        db.session.commit()
        return redirect(url_for('products.product_home'))

    sections = Section.query.all()
    return render_template('products/edit_product.html', products=products, sections=sections)



@product_blueprint.route('/product/<int:product_id>', methods=['GET'])
def product_details(product_id):
    product = Product.query.get(product_id)
    return render_template('products/product_details.html', product=product)



@product_blueprint.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        db.session.delete(product)  # Delete the specific product instance
        db.session.commit()

        return redirect(url_for('products.product_home'))

    return render_template('products/delete_product.html', product=product)
