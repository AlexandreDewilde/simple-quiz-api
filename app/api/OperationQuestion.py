from flask_restful import Resource
from . Question import Question
from . MultipleChoiceQuestion import MultipleChoiceQuestion
from flask_jwt import JWT, jwt_required
from . User import *

class ShowQuestion(Resource):
	def get(self, question_id):
		return Question().show_question(question_id)

class ShowMultipleChoiceQuestion(Resource):
	def get(self, question_id):
		return MultipleChoiceQuestion().show_question(question_id)

class CreateQuestion(Resource):
	@jwt_required()
	def post(self):
		return Question().create_question()
class CreateMultipleChoiceQuestion(Resource):
	@jwt_required()
	def post(self):
		return MultipleChoiceQuestion().create_question()

class DeleteQuestion(Resource):
	def post(self):
		return Question().delete_question()

class DeleteMultipleChoiceQuestion(Resource):
	def post(self):
		return MultipleChoiceQuestion().delete_question()