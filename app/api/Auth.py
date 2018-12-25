from flask_jwt_simple import JWTManager, jwt_required, create_jwt, get_jwt_identity
from flask import jsonify, Flask, request

def auth():
	"""returns tokens to auth"""
	if not request.is_json:
		return jsonify({"status": "Missing JSON in request"}), 400

	params = request.get_json()
	username = params.get('username', None)
	password = params.get('password', None)

	if not username:
		return jsonify({"status": "Missing username parameter"}), 400
	if not password:
		return jsonify({"status": "Missing password parameter"}), 400

	if username != 'admin' or password != 'admin':
		return jsonify({"status": "Bad username or password"}), 401

	ret = {'jwt': create_jwt(identity=username)}
	return jsonify(ret), 200