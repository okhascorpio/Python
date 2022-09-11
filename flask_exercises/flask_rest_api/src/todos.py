from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database import db, Users, Todos


todos = Blueprint("todos", __name__, url_prefix="/api/v1/")


@todos.route('/todos', methods=['POST', 'GET'])
@jwt_required()
def todo_items():


        current_user = get_jwt_identity()
        if request.method == 'POST':
                user_id = get_jwt_identity()
                name = request.json.get('name', '')
                description = request.json.get('description', '')
                status = request.json.get('status','NotStarted')
                todo_item = Todos(user_id=current_user, name=name, description=description, status=status)

                db.session.add(todo_item)
                db.session.commit()

                return {'message': 'todo item added'}
        else:
                #user_id = get_jwt_identity()
                todo_items = Todos.query.filter_by(user_id=current_user)
                data = []
                for todo_item in todo_items:
                        data.append({'item name': todo_item.name, 'status':todo_item.status})
        return jsonify({'items': data})


