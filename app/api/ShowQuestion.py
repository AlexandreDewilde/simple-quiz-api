from flask_restful import Resource
from . Question import Question

class ShowQuestion(Resource):
	def get(self, question_id):
		return Question().show_question(question_id)

