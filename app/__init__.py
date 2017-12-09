from flask import Flask
from flask_bootstrap import Bootstrap       
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask (__name__)

    #this part is creating app configuration

    app.config.from_object(config_options[config_name])

    #initializing flask extensions 

    bootstrap.init_app(app)

    #this part helps to register the blueprint
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)    

    # setting the config 

    from .requests import config_func
    config_func(app)
    
    return app