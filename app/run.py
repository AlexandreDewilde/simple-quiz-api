import json 
from flask import jsonify, Flask, request
from api.Question import Question
from api.MultipleChoiceQuestion import MultipleChoiceQuestion
from flask_jwt_simple import JWTManager, jwt_required, create_jwt
from api import Auth


#create instance of flaskq
app = Flask(__name__)

# Setup the Flask-JWT-Simple extension
app.config["JWT_SECRET_KEY"] = "a simple super-secret" 
jwt = JWTManager(app)

#add to route auth
@app.route("/auth", methods=["POST"])
def auth():
	return Auth.auth()

def jwt_cond(jwt_required, cond):
	def decorator(func):
		if not cond:
			return func
		return jwt_required(func)
	return decorator

#add to route the classes for simple question
@app.route("/show-all-question")
@jwt_cond(jwt_required, False)
def show_all_question():
	return jsonify(Question().show_all_question())

#show all the categories for the simple questions
@app.route("/show-all-categories")
@jwt_cond(jwt_required, False)
def show_categories():
	return jsonify(Question().show_categories())

@app.route('/show-question/<int:question_id>')
@jwt_cond(jwt_required, False)
def show_question(question_id):
	return jsonify(Question().show_question(question_id))

@app.route('/add-question', methods=['POST'])
@jwt_cond(jwt_required, True)
def add_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	post_data = request.data
	data = json.loads(post_data)
	return jsonify(Question().add_question(data))

@app.route("/update-question", methods=["POST"])
@jwt_cond(jwt_required, True)
def update_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	post_data = request.data
	data = json.loads(post_data)
	return jsonify(Question().update_question(data))

@app.route('/delete-question', methods=['POST'])
@jwt_cond(jwt_required, True)
def delete_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	data = request.data
	question_id = json.loads(data)['id']
	return jsonify(Question().delete_question(question_id))


#add to route classes for mutilple choice question
@app.route("/show-all-multiple-choice-question")
@jwt_cond(jwt_required, False)
def show_all_multiple_choice_question():
	return jsonify(MultipleChoiceQuestion().show_all_question())

#show all categories for multiple choice question
@app.route('/show-all-categories-multichoice')
@jwt_cond(jwt_required, False)
def show_categories_multiple_choice():
	return jsonify(MultipleChoiceQuestion().show_categories())

@app.route('/show-multiple-choice-question', methods=['GET'])
@jwt_cond(jwt_required, False)
def show_multiple_choice_question(question_id):
	return jsonify(MultipleChoiceQuestion().show_question(question_id))

@app.route('/add_multiple-choice-question', methods=['POST'])
@jwt_cond(jwt_required, True)
def add_multiple_choice_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	post_data = request.data
	data = json.loads(post_data)
	if "choice" not in data:
		return jsonify({"status":"you must specify a list of choice"})
	return jsonify(MultipleChoiceQuestion().add_question(data))

@app.route("/update-question-multiple-choice-question", methods=["POST"])
@jwt_cond(jwt_required, True)
def update_multiple_choice_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	post_data = request.data
	data = json.loads(post_data)
	return jsonify(Question().update_question(data))

@app.route('/delete_multiple-choice-question', methods=['POST'])
@jwt_cond(jwt_required, True)
def delete_multiple_choice_question():
	if not request.is_json:
		return jsonify({
			"status":"Body must be json"
		})
	data = request.data
	question_id = json.loads(data)['id']
	return jsonify(MultipleChoiceQuestion().delete_question(question_id))

if __name__ == "__main__":
	app.run(debug=False)