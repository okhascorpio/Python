#Flask exercise:

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

print (os.environ.get('Test'))
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)