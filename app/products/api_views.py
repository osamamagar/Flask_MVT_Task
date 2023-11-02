from flask_restful import Resource,fields,marshal_with,abort
from flask import make_response
from app.models import Product,Section,db
from app.products.parser import product_parser






sections_Serialixer = {
    'id':fields.Integer,
    'name':fields.String
}

products_serializer = {
    'id':fields.Integer,
    'name':fields.String,
    'section_id':fields.Integer,
    'section':fields.Nested(sections_Serialixer)
}



class ProductList(Resource):
    @marshal_with(products_serializer)
    def get(self):
        products = Product.get_all_objects()
        return products,200
    

    @marshal_with(products_serializer)
    def post(self):
        args = product_parser.parse_args()

        product = Product(
            name=args['name'],
            section_id=args['section_id'],
            image=args['image']
        )

        product.save_product()

        return product, 201

class ProductEdit(Resource):
    @marshal_with(products_serializer)
    def put(self, product_id):
        args = product_parser.parse_args()

        product = Product.get_specific_product(product_id)
        product.name = args['name']
        product.section_id = args['section_id']
        product.image = args['image']

        db.session.commit()

        return product, 200



class ProductDelete(Resource):
    def delete(self, product_id):
        product = Product.get_specific_product(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            response = make_response("Product was deleted successfully", 204)
            return response
        
        abort(404)
class CustomProduct(Resource):
    def get(self, product_id):
        product = Product.get_specific_product(product_id)
        if product:
            return {
                'message': 'Custom product route for product with ID {}'.format(product_id),
                'product_name': product.name,
                'product_section': product.section.name
            }, 200
        else:
            return {'message': 'Product not found'}, 404
