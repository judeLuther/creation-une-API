from flask import Flask

from config import Config
from app.extensions import db

# In this code, a function named create_app is defined, which is 
# responsible for creating and configuring a Flask application instance.

# This code follows the common pattern of using a factory function (create_app) to create 
# and configure the Flask application. This allows for better organization, 
# reusability, and testability of the application code.


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()

    return app