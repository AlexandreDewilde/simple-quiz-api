from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
class UpdateQuestion():
	def post(self):
		parser.add_argument('id', required=True, type=str)
		parser.add_argument('new_question', required=True)
		args = parser.parse_args()
		