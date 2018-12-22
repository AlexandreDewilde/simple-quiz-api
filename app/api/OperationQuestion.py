from flask_restful import Resource
from . Question import Question
from . MultipleChoiceQuestion import MultipleChoiceQuestion


class ShowQuestion(Resource):
	def get(self, question_id):
		return Question().show_question(question_id)

class ShowMultipleChoiceQuestion(Resource):
	def get(self, question_id):
		return MultipleChoiceQuestion().show_question(question_id)

class CreateQuestion(Resource):
	def post(self):
		return Question().create_question()
class CreateMultipleChoiceQuestion(Resource):
	def post(self):
		return MultipleChoiceQuestion().create_question()

class DeleteQuestion(Resource):
	def post(self):
		return Question().delete_question()

class DeleteMultipleChoiceQuestion(Resource):
	def post(self):
		return MultipleChoiceQuestion().delete_question()