from flask import Flask
from app.models import db
from app.config import projectConfig
from app.products import product_blueprint


def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = projectConfig[config_name]
    # app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)
    app.register_blueprint(product_blueprint)

    return app
