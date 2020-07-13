import mongoengine as me
from flask_mongoengine.wtf import model_form

class Location(me.EmbeddedDocument):
    latitude = me.LongField(required=True)
    longitude = me.LongField(required=True)

# class Item(me.EmbeddedDocument):
#     type = me.StringField(required=True)
#     quantity = me.IntField()

class AskPost(me.EmbeddedDocument):
    _id = me.ObjectIdField(required=True)
    postID = me.ObjectIdField(required=True)
    #asking = me.BooleanField(required=True)
    item = me.StringField(required=True)
    created = me.DateTimeField(required=True)
    explanation = me.StringField(required=True)
    radius = me.IntField(required=True)

class GivePost(me.EmbeddedDocument):
    _id = me.ObjectIdField(required=True)
    postID = me.ObjectIdField(required=True)
    #asking = me.BooleanField(required=True)
    item = me.StringField(required=True)
    created = me.DateTimeField(required=True)
    explanation = me.StringField(required=True)
    radius = me.IntField(required=True)

class User(me.Document):
    _id = me.ObjectIdField(required=True)
    userID = me.ObjectIdField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    username = me.StringField(required=True)
    firstName = me.StringField(required=True)
    lastName = me.StringField(requried=True)
    phone = me.StringField(required=True)
    created = me.DateTimeField(required=True)
    location = me.EmbeddedDocumentField(Location)
    rating = me.LongField()
    askPosts = me.EmbeddedDocumentListField(AskPost)
    givePosts = me.EmbeddedDocumentListField(GivePost)