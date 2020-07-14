from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from datetime import datetime

import json


app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

with open('./credentials.json') as file:
    credentials = json.load(file)

app.config['JWT_SECRET_KEY'] = credentials['secret-key']

from bson.objectid import ObjectId
import mongo

from models import User, AskPost, GivePost, Location



#TODO: add try-catches
  
#Add post to user's giveposts
#POST args: username, item, explanation, radius
#Return response w/ message and status code
@app.route('/user/post', methods=['POST'])
def create_givepost():
    postData = request.get_json()
    item = postData['item']
    explanation = postData['explanation']
    radius = postData['radius']
    username = postData['username']
    postType = postData['post-type']
    id = ObjectId()
    postID = ObjectId()

    created = datetime.utcnow()

    #TODO handle non-existent username
    if postType=='give':
        post = GivePost(_id = id, postID=postID, item=item, explanation=explanation, radius=radius, created=created)
        user = User.objects.get(username=username)
        user.givePosts.append(post)
    elif postType=='ask':
        post = AskPost(_id = id, postID=postID, item=item, explanation=explanation, radius=radius, created=created)
        user = User.objects.get(username=username)
        user.askPosts.append(post)
    else:
        error = jsonify({
            'error': 'Invalid post type'
        })
        return Response(error, mimetype='application/json', status=400)

    user.save()

    return Response(user.to_json(), mimetype='application/json', status=200)


#Login to database. POST to database to get user information and validate password
#Returns error code if unsuccessful or access token if successful
@app.route('/user/login_user', methods=['POST'])
def login_user():
    email = request.get_json()['email']
    password = request.get_json()['password']

    user = User.objects.get(email=email)

    if bcrypt.check_password_hash(user['password'], password) == 0:
        result = jsonify({
            'error': 'Invalid username and password'
        })
    else:
        access_token = create_access_token(identity = {'firstName': user['firstName'], 'lastName': user['lastName'], \
                                           'email': user['email'], '_id': str(user['_id']), 'userID': str(user['userID'])})
        result = jsonify({'token': access_token})

    return result


#Register a user. POST User to database. Have user info as arguments in JSON format in post 
#POST args: username, item, explanation, radius
#Return response w/ message and status code
@app.route('/user/register_user', methods=['POST'])
def register_user():
    id = ObjectId()
    userID = ObjectId()
    username = request.get_json()['username']
    phone = request.get_json()['phone']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    firstName = request.get_json()['first-name']
    lastName = request.get_json()['last-name']
    locationObj = request.get_json()['location']
    created = datetime.utcnow()

    location = Location(country=locationObj['country'], state=locationObj['state'], city=locationObj['city'], \
        latitude=locationObj['latitude'], longitude=locationObj['longitude'], zipcode=locationObj['zipcode'])


    if User.objects(username=username):
        error = jsonify(
            {
                'error': 'Username is taken'
            }
        )
        return Response(error, mimetype='application/json', status=200)

    user = User(_id=id, userID=userID, username=username, email=email, password=password, \
                phone=phone, firstName = firstName, lastName = lastName, created=created, location=location)

    user.save()

    return Response(user.to_json(), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True)