#__author__ == "Chen Li"


##### Setup #####

# Import packages to be used
import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

##### Set up Models #####
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    US_gross = db.Column(db.Integer, nullable = True)
    world_gross = db.Column(db.Integer, nullable = True)
    production_budget = db.Column(db.Integer, nullable = True)
    release_date = db.Column(db.String(64), nullable = True)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    age = db.Column(db.String(64), nullable = True)
    nationality = db.Column(db.String(64), nullable = False)

class Genre(db.Genre):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)


##### Set up Controllers (route functions) #####

#Route1 Create a new movie

#Route2 Show query result of all movies of a certain genre

#Route3 Show a random movie which exists in the database



if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
