from flask import Flask, Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from src.database import db, Users
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token, create_access_token

auth = Blueprint("auth", __name__, url_prefix="/api/v1/")


@auth.post('/signup')
def sign_up():

    # Post jason data, email and password  {"email":"example@example.com","password":"YourPassword}"

    email = request.json.get('email', '')
    password = request.json.get('password', '')

    if Users.query.filter_by(email=email).first() is not None:
        return {'error': 'Email is taken'}

    pwd_hash = generate_password_hash(password)

    user = Users(email=email, password=pwd_hash)

    db.session.add(user)
    db.session.commit()

    return {'message': 'User created'}


@auth.post('/signin')
def sign_in():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    user = Users.query.filter_by(email=email).first()

    # If user exists:
    if user:
        # if password is correct:
        pass_check = check_password_hash(user.password, password)
        # if password hash match the stored data
        if pass_check:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)
            # return {'message':'Login Successful'}
            return {
                'user': {
                    'access': access,
                    'user': user.email
                }



            }
        else:
            return {'message': 'incorrect Password'}
    else:
        return "User not found"


@auth.put('/changePassword:')
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    new_password = request.json.get('password', '')
    if new_password == '':
        return {'error': 'password cannot be empty'}
    else:
        user = Users.query.filter_by(id=user_id).first()
        return {'user email': user.email}
