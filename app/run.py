from flask import jsonify, Flask, request
from api.Question import Question
from api.MultipleChoiceQuestion import MultipleChoiceQuestion
import json 


#create instance of flaskq
app = Flask(__name__)

#add to route the classes for simple question
@app.route("/show-all-question")
def show_all_question():
	return jsonify(Question().show_all_question())

@app.route('/show-question/<int:question_id>')
def show_question(question_id):
	return jsonify(Question().show_question(question_id))

@app.route('/add-question', methods=['POST'])
def add_question():
	post_data = request.data
	data = json.loads(post_data)
	return jsonify(Question().add_question(data))

@app.route('/delete-question', methods=['POST'])
def delete_question():
	data = request.data
	question_id = json.loads(data)['id']
	return jsonify(Question().delete_question(question_id))


#add to route classes for mutilple choice question
@app.route("/show-all-multiple-choice-question")
def show_all_multiple_choice_question():
	return jsonify(MultipleChoiceQuestion().show_all_question())

@app.route('/show-multiple-choice-question', methods=['GET'])
def show_multiple_choice_question(question_id):
	return jsonify(MultipleChoiceQuestion().show_question(question_id))

@app.route('/add_multiple-choice-question', methods=['POST'])
def add_multiple_choice_question():
	post_data = request.data
	data = json.loads(post_data)
	if "choice" not in data:
		return jsonify({"status":"you must specify a list of choice"})
	return jsonify(MultipleChoiceQuestion().add_question(data))

@app.route('/delete_multiple-choice-question', methods=['POST'])
def delete_multiple_choice_question():
	data = request.data
	question_id = json.loads(data)['id']
	return jsonify(MultipleChoiceQuestion().delete_question(question_id))

if __name__ == "__main__":
	app.run(debug=True)