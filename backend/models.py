import mongoengine as me

class Post(me.EmbeddedDocument):
    postID = me.IntField(required=True)
    asking = me.BooleanField(required=True)
    food = me.StringField(required=True)
    location = me.LongField(required=True)
    time = me.DateTimeField(required=True)
    explanation = me.StringField(required=True)
    radius = me.IntField(required=True)

class User(me.Document):
    userID = me.IntField(required=True)
    name = me.StringField(required=True)
    phone = me.StringField(required=True)
    location = me.LongField(required=True)
    type_help = me.StringField(required=True)
    rating = me.LongField(required=True)
    posts = me.EmbeddedDocumentListField(Post)