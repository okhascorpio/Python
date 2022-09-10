Exercise with flask:

installed pip environment "pip install pipenv"
launched pip shell "pipenv shell"
installed dependencies " pipenv install psycopg2 flask flask-sqlalchemy"

make new database named "TODO" in pgAdmin4

in console write py
"from app import db"
"db.create_all()"

run app.py

open the webpage on localhost, enter data and send.

check database TODO>tables>users>view/edit data, to view entered data.

