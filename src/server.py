from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import dbConnectionHandler

dbConnectionHandler.connectDb()

app = Flask(__name__)
CORS(app)

from src.main.event_routes import eventRouteBp

app.register_blueprint(eventRouteBp)