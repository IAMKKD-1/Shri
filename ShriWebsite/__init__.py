from flask import Flask
import os

def index():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    
    from .views import views
    from .auth import auth
    from .models import create_table
    
    create_table(table='Users',
    columns="""(id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255),
    date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)""")

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    return app