#Flask exercise:

from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:onefour@localhost/TODO'
app.config['SECRET_KEY'] = 'SecretKey124'
db=SQLAlchemy(app)

#class users(db.Model):
 #  __tablename__='users'
 # id=db.Column(db.Integer,primary_key=True)
 # email=db.Column(db.String(40), unique=True)
 # password=db.Column(db.String(40))

 # def __init__(self,email,password):
 #   self.email=email
 #   self.password=password


class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    todo = db.relationship('TODO', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.email}'


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])

def submit():
  email= request.form['email']
  password=request.form['password']

  user=users(email,password)
  db.session.add(user)
  db.session.commit()

  #fetch a certain student2
  userResult=db.session.query(users).filter(users.id==1)
  for result in userResult:
    print(result.email)

  return render_template('success.html', data=email)



if __name__ == '__main__':
    app.run(debug=True)