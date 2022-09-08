#Flask exercise:

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:onefour@localhost/TODO'

db=SQLAlchemy(app)

class users(db.Model):
  __tablename__='users'
  id=db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(40))
  password=db.Column(db.String(40))

  def __init__(self,email,password):
    self.email=email
    self.password=password


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