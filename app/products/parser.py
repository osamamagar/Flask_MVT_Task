from flask_restful import reqparse


# product_parser= reqparse.RequestParser()
# product_parser.add_argument('name',type=str,required = True,help='Product is Required')
# product_parser.add_argument('image',type=str)
# product_parser.add_argument('imsection_idage',type=int)
product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True, help='Product name is required')
product_parser.add_argument('section_id', type=int, required=True, help='Section ID is required')
product_parser.add_argument('image', type=str)
