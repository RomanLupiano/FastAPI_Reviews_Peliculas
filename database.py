from peewee import MySQLDatabase, Model, CharField, DateTimeField, ForeignKeyField, IntegerField, TextField
from datetime import datetime
import hashlib
from os import getenv
from dotenv import load_dotenv

load_dotenv()

database = MySQLDatabase(getenv('DATABASE_NAME'), 
                         user=getenv('DATABASE_USER'), 
                         password=getenv('DATABASE_PASSWORD'), 
                         host=getenv('DATABASE_HOST'), 
                         port=int(getenv('DATABASE_PORT')))


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.username
    
    class Meta:
        database = database
        table_name = 'user'
    
    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()
    

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title
    
    class Meta:
        database = database
        table_name = 'movie'


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f'{self.movie.title} - {self.user.username}'
    
    class Meta:
        database = database
        table_name = 'user_review'