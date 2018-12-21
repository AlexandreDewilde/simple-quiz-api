from flask_restful import Resource
from . Question import Question

class CreateQuestion(Resource):
	def post(self):
		return Question().create_question()