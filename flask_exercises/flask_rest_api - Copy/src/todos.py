from flask import Blueprint, request, jsonify 
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database import db, Users, Todos, STATUS
from datetime import date, datetime

# todos blueprint
todos = Blueprint("todos", __name__, url_prefix="/api/v1/")


@todos.route('/todos', methods=['POST', 'GET'])
@jwt_required()
def todo_items():

    current_user = get_jwt_identity()

    # Handle POST requests ie create new todo item
    if request.method == 'POST':
        # name is necessary
        name = request.json.get('name', '')
        if name == '':
            return {'error': 'name cannot be empty'}
        # optional description
        description = request.json.get('description', '')
        # optional status, default status is NotStarted
        status = request.json.get('status', 'NotStarted')
        if STATUS.has_key(status) == False:
            return {'error': "can only be one of these 'OnGoing','NotStarted','Completed'"}

        todo_item = Todos(user_id=current_user, name=name,
                          description=description, status=status)

        db.session.add(todo_item)
        db.session.commit()

        return {'message': 'todo item added'}

    # Handel Get requests
    else:
        if 'status' in request.args:  # parameter is specified
            status = request.args.get('status', type=str)

            # import STATUS from database and search given argument in it
            if STATUS.has_key(status):
                todo_items = Todos.query.filter_by(
                    user_id=current_user, status=status)
            else:
                return {'error': "argument can only be one of these 'OnGoing','NotStarted','Completed'"}

        # if no parameter named 'status' is given return all items
        else:
            todo_items = Todos.query.filter_by(user_id=current_user)

        data = []
        for todo_item in todo_items:
            data.append(
                {'id': todo_item.id,
                 'user': todo_item.user_id,
                 'name': todo_item.name,
                 'description': todo_item.description,
                 'status': todo_item.status
                 }
            )
        return jsonify({'items': data})


# Handel PUT requests
@todos.put("/todos:<int:id>")
@jwt_required()
def get_todo_item(id):
    current_user = get_jwt_identity()

    todo_item = Todos.query.filter_by(user_id=current_user, id=id).first()

    if not todo_item:
        return {
            'error': 'todo item not found, send correct id'
        }
    # if item is found we can update its fields
    else:

        name = request.json.get('name', '')

        # optional description
        description = request.json.get('description', '')
        # optional status, default status is NotStarted
        status = request.json.get('status', 'NotStarted')
        if STATUS.has_key(status) == False:
            return {'error': "can only be one of these 'OnGoing','NotStarted','Completed'"}
        else:
                todo_item.name=name
                todo_item.description=description
                todo_item.status=status
                todo_item.updated_at=datetime.now()
                db.session.commit()

        return {
            'id': todo_item.id,
            'user': todo_item.user_id,
            'name': todo_item.name,
            'description': todo_item.description,
            'status': todo_item.status
        }
