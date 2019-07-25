from google.appengine.ext import ndb

class User(ndb.Model):
	email = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)


class Events(ndb.Model):
	date = ndb.StringProperty(required=True)
	time = ndb.IntegerProperty(required=True)


