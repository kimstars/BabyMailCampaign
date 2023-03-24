import os, sys
import requests
from flask import Flask, redirect, url_for, request, render_template



from config import ProdConfig

# login manager
from flask_login import LoginManager

# import models and create tables in database
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_name):
    # initialize app and configure global objects
    app = Flask(__name__,
                static_url_path='/assets', 
                static_folder='assets',
                template_folder='templates')

    # configure app
    app.config.from_object(ProdConfig)

    from models import db
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("create db done")
         # import blueprints
        from mailcamp.routes import mailcamp
        from users.routes import users
        
        
        app.register_blueprint(mailcamp)
        app.register_blueprint(users)
        
    return app