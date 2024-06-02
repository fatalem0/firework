from flask_restx import Api
from flask import Blueprint, Flask
from src.db import db, flask_bcrypt
from src.config import config_by_name
from flask.app import Flask
from flask_cors import CORS

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns
from .controller.client_controller import api as client_ns
from .controller.tests_controller import api as test_ns
from .controller.consultation_card_controller import api as consultation_card_ns

blueprint = Blueprint("api", __name__)
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    blueprint,
    title="FIREWORK",
    version="1.0",
    description="firework project",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(user_ns, path="/user")
api.add_namespace(client_ns, path="/client")
api.add_namespace(consultation_card_ns, path="/card")
api.add_namespace(test_ns, path="/test")
api.add_namespace(auth_ns)

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    CORS(app)

    return app
