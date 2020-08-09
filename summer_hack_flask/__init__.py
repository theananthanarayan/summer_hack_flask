from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_googlemaps import GoogleMaps
#from flask_jwt_extended import JWTManager
#from flask_jwt_extended import create_access_token
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
import json



with open("./credentials.json") as file:
    credentials = json.load(file)


app = Flask(__name__)
app.config['SECRET_KEY'] = credentials['secret-key']
app.config['GOOGLEMAPS_KEY'] = credentials['maps_key']

Bootstrap(app)
CORS(app)
googleMaps = GoogleMaps(app)

DB_URI = "mongodb+srv://" + credentials["mongodb"]["username"] + ":" + credentials["mongodb"]["password"] + "@summerhack2020.iuqak.azure" + ".mongodb.net/test" + "?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI
db = MongoEngine(app)

bcrypt = Bcrypt(app)
#jwt = JWTManager(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from summer_hack_flask import routes




