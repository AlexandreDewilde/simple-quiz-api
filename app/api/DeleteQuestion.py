from flask_restful import Resource
from . Question import Question

class DeleteQuestion(Resource):
	def post(self):
		return Question().delete_question()