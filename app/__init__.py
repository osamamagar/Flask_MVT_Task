from flask import Flask
from app.models import db
from app.config import projectConfig
from app.products import product_blueprint
from app.sections import section_blueprint
from flask_migrate import Migrate
from flask_restful import Api
from app.products.api_views import ProductList,ProductDelete,ProductEdit,CustomProduct

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = projectConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(section_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    api = Api(app)
    api.add_resource(ProductList,'/api/products')
    api.add_resource(ProductEdit, '/api/products/<int:product_id>')
    api.add_resource(ProductDelete, '/api/products/<int:product_id>')
    api.add_resource(CustomProduct, '/api/products/<int:product_id>')




    return app
