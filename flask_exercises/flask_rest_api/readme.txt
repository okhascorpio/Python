Add your postgresql credentials in .env file

enter the virtualenv
$ . venv/Scripts/activate

Create database by running commands:
$ flask shell
$ from src.database import db 
$ db.create_all()




Run the app
$ flask run

Use Postman to send to create user:
localhost:5000/api/v1/signup
{
"email":"user1@hello.com",
"password":"one"
}
Response:
{
    "message": "User created"
}


Send signin request using registered credentials:
localhost:5000/api/v1/signin
{
"email":"user1@hello.com",
"password":"one"
}

response received JWT access token for the user:
{
 "user": {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MjkxNTk4NSwianRpIjoiNzQ2MjhmMTktNmU3Ni00ODNiLTk0NmYtZmEwNzc5OTNmYTlhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjYyOTE1OTg1LCJleHAiOjE2NjI5MTY4ODV9.QbqiNlkrT3hyQdGQSNkJxkDaL7SwhDOC1SClmyj_MME",
        "user": "user1@hello.com"
    }
}













