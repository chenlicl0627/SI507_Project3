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
    title = db.Column(db.String(250), nullable = False)
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
    age = db.Column(db.Integer, nullable = True)
    nationality = db.Column(db.String(64), nullable = False)
    movies = db.relationship('Movie', backref='Director')

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    movies = db.relationship("Movie", backref = "Genre")

##### Helper functions #####
def get_or_create_director(name, age, nationality):
    director = Director.query.filter_by(name=name,nationality=nationality).first()
    if director:
        return director
    else:
        new_director = Director(name=name, age=age, nationality=nationality)
        session.add(new_director)
        session.commit()
        return new_director

def get_or_create_genre(genre):
    the_genre = Genre.query.filter_by(name=genre).first()
    if the_genre:
        return the_genre
    else:
        new_genre = Genre(name=genre)
        session.add(new_genre)
        session.commit()
        return new_genre

# # Test out the function
# get_or_create_director("Christopher Nolan", 48, "United Kingdom; United States")
# get_or_create_director("Nolan", 48, "UK")
# get_or_create_genre("Thriller")

##### Set up Controllers (route functions) #####


#Route1 Test Route
@app.route('/')
def greeting():
    return "Hello everyone!"

#Route2 Create a new movie
@app.route('/movie/new/<title>/<US_gross>/<world_gross>/<production_budget>/<release_date>/<director>/<director_age>/<director_nation>/<genre>')
def new_movie(title, US_gross, world_gross, production_budget, release_date, director,director_age,director_nation,genre):  ## QUESTION:Can I somehow apply the technique of keeping the code simple and clean used in the movie_tools_clean.py firle here?

    movie_director = get_or_create_director(director, director_age, director_nation)
    movie_genre = get_or_create_genre(genre)
    # return movie_genre.name

    if Movie.query.filter_by(title=title, director_id=movie_director.id).first(): ## Check whether a name with the same name and director has already existed.
        return "The movie already exists."
    else:
        new_movie = Movie(title=title, US_gross=US_gross, world_gross=world_gross, production_budget=production_budget, release_date=release_date, director_id=movie_director.id, genre_id=movie_genre.id)# Add the movie to the database
        session.add(new_movie)
        session.commit()
        return "A new movie is added: {} by {}.".format(new_movie.title, movie_director.name)

#Route3 Show query result of all movies of a certain genre
@app.route('/movies/<genre>')
def see_genre(genre):
    selected_genre = get_or_create_genre(genre)
    movies_of_genre = Movie.query.filter_by(genre_id=selected_genre.id).all()
    # return "hello"
    # ## debug ends
    result = ""
    for m in movies_of_genre:
        result += "{}|{}".format(m.title,selected_genre.name)+ "<br>"
    return result


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python SI507_project3.py runserver
