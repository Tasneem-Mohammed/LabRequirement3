from flask import request, jsonify

TOKEN = 'secretToken'

def authorize_the_token():
    token = request.headers.get('Authorization')
    if not token or token != f"Bearer {TOKEN}": 
        return jsonify({"error": "Unauthorized"}), 401
