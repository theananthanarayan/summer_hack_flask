from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from main import app
import json

from models import User

with open("./credentials.json") as file:
    credentials = json.load(file)


DB_URI = "mongodb+srv://" + credentials["mongodb"]["username"] + ":" + credentials["mongodb"]["password"] + "@" + credentials["mongodb"]["database-name"] + ".mongodb.net/test" + "?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)