# The SQLAlchemy class is a central component of SQLAlchemy and 
# represents the database connection and ORM functionality. 
# By creating an instance of this class, we can interact with the 
# database and define models that map to database tables.

from flask_sqlalchemy import SQLAlchemy

# Initialize a SQLAlchemy instance
db = SQLAlchemy()