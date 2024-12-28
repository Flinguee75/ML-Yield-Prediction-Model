from flask import Flask
from .config import Config
from .scripts.models import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    init_app(app)
    
    return app
