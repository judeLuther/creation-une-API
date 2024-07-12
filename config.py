import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASK_DEBUG = True
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    #     or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    if 'RDS_DB_NAME' in os.environ:
        SQLALCHEMY_DATABASE_URI = \
        'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        username=os.environ['RDS_USERNAME'],
        password=os.environ['RDS_PASSWORD'],
        host=os.environ['RDS_HOSTNAME'],
        port=os.environ['RDS_PORT'],
        database=os.environ['RDS_DB_NAME'],
        )
    else:
        username = 'diotsiaci'
        password = 'diotsiaci2we'
        database = 'diotsiaci'
        SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@localhost:5432/{database}"


    #SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@localhost:5432/{database}"
