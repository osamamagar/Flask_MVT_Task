
from flask import Blueprint

section_blueprint = Blueprint('sections', __name__ , url_prefix='/sections')

from app.sections import views