from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # creating the application configurations
    app.config.from_object(Config_options[config_name])

    # initializing bootstrap extension
    bootstrap.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app
