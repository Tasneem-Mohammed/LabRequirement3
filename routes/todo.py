from flask import Blueprint, jsonify, request
from middleware.authorization import authorize_the_token

todos_bp = Blueprint('todos', __name__)

todos = []

@todos_bp.before_request
def before_request():
    authorize_the_token()

@todos_bp.route('/', methods=['GET'])
def get_todos():
    return jsonify(todos)

@todos_bp.route('/', methods=['POST'])
def add_todo():
    todo = {
        'id': len(todos) + 1, 
        'task': request.json.get('task'),
        'completed_task': request.json.get('completed_task', False)
    }
    todos.append(todo)
    return jsonify(todos), 201

@todos_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Task not found'}), 404
    todo['task'] = request.json.get('task', todo['task'])
    todo['completed_task'] = request.json.get('completed_task', todo['completed_task'])
    return jsonify(todo)

@todos_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Task not found'}), 404
    todos.remove(todo)
    return jsonify({'message': 'Task has been deleted successfully'}), 204

