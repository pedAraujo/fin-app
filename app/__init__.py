from flask import Flask
from .routes import main
from .auth import auth
from .dash import init_dash_app
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def create_flask_server():
    server = Flask(__name__)
    server.config.from_pyfile("config.py")

    with server.app_context():
        server.register_blueprint(main)
        server.register_blueprint(auth)
        init_dash_app(server)
        return server
