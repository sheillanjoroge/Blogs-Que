from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet,configure_uploads
from flask_mail import Mail





login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)



    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    

    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)
    # configure UploadSet
    configure_uploads(app,photos)
    
    mail.init_app(app)

    return app