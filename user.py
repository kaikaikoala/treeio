from peewee import *
from flask_login import UserMixin
import datetime

database = MySQLDatabase('TreeIO', **{'user': 'root'})

def before_request_handler():
    database.connect()
    
def after_request_handler():
    database.close()

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Members(UserMixin,BaseModel):
    email = CharField(unique=True, null=True)
    memid = PrimaryKeyField()
    name = CharField(null=True)
    password = CharField(null=True)
    school = IntegerField(null=True)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default = False)
    shortname = CharField(null=True)

    class Meta:
        db_table = 'members'

class Organizations(UserMixin,BaseModel):
    city = CharField(null=True)
    email = CharField(null=True)
    name = CharField(null=True)
    orgid = PrimaryKeyField()
    orgtype = CharField(null=True)
    password = CharField(null=True)
    shortname = CharField(null=True)
    state = CharField(null=True)
    zipcode = IntegerField(null=True)

    class Meta:
        db_table = 'organizations'