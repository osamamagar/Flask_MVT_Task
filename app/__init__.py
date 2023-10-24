from flask import Flask
from app.models import db
from app.config import projectConfig
from app.products import product_blueprint
from app.sections.views import all_sections
from app.sections import section_blueprint
from flask_migrate import Migrate

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = projectConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(section_blueprint)
    app.add_url_rule('/sections', view_func=all_sections, endpoint='all_sections')

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    return app
