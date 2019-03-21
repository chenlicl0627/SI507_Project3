# SI507 Project 3

## What this program can do?

This program can present the information about a movie database on website based on users' input.

More specifically, it displays the following information:

1. Go to `127.0.0.1:5000/` and you will see a general greeting that says Hello everyone!"
2. Go to `127.0.0.1:5000/movie/new/<title>/<US_gross>/<world_gross>/<production_budget>/<release_date>/<director>/<director_age>/<director_nation>/<genre>` to create a new movie based on the information provided in the url.
3. Go to `127.0.0.1:5000/movies/<genre>` with a genre name at your choice and the webpage will display all movies in the database which belong to the genre specified.

## What is the project structure?

The project contains multiple files. `README.md` (this file) is the description of the project. `requirements.txt` is used to help you install all dependencies of the project. `SI507_project3.py` contains the main program, including database structure definition, flask route definition, etc.

## What are the dependencies?

You can install everything you need by using the included `requirements.txt` file.

Make sure you have `virtualenv` installed. If you don't, use the following command to install `virtualenv`:

> pip install virtualenv

Then, `cd` to the project directory and activate `virtualenv`:

> source venv/bin/activate

Then, you can install this project's dependencies:

> pip install -r requirements.txt

## How to run the project?

After you have your dependencies installed, run the following commands:

> python SI507_project3.py runserver

Then, you can check out the following URLs at your choice:

http://127.0.0.1:5000

http://127.0.0.1:5000//movie/new/<title>/<US_gross>/<world_gross>/<production_budget>/<release_date>/<director>/<director_age>/<director_nation>/<genre>

http://127.0.0.1:5000/movies/<genre>
