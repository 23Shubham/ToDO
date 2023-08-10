from flask import Flask, request
from .utils.config import BaseConfig
from .database import db
from .models import *
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
base_data = BaseConfig()

app.config['SQLALCHEMY_DATABASE_URI'] = base_data.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = base_data.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)


def create_app():
    with app.app_context():
        db.create_all()
    from app.routes import main_app
    app.register_blueprint(main_app)
    return app
