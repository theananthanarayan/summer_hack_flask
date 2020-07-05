from flask import Flask


app = Flask(__name__)

import db
from models import User

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/help')
def help():
    return 'help'

#test POST to database
@app.route('/test')
def test():
    test_model = User(name="test", phone="test", location=2.2, type_help = "sdaf", rating=12.2, userID=1)
    test_model.save()
    return "Connected to the data base!"

if __name__ == '__main__':
    app.run(debug=True)


