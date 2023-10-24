
from app.products import product_blueprint


@product_blueprint.route('hello')
def hello():
    return '<h2> osama magar </h2>'
