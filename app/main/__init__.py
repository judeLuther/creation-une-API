from flask import Blueprint

# Create a Blueprint instance named 'main'
# A Blueprint is a way to organize related routes, views, 
# and other application components into modular units.
bp = Blueprint('main', __name__)

from app.main import routes