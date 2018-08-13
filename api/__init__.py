from flask import Flask
from flask_cors import CORS
from instance.config import app_config
from flask_restful import Api
from api.endpoints import TicTacToe


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    api = Api(app=app)
    CORS(app)

    api.add_resource(
        TicTacToe, "/",
        "/", endpoint="home"
    )

    return app


app = create_app('development')
