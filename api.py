import flask
from flask_restful import Resource, Api, reqparse
import json


#create instance of flaskapp = flask.Flask(__name__)
api = Api(app)

#open questions.json files
with open('questions.json', 'r') as json_file:
	questions = json.load(json_file) 

class Questions(Resource):
	def get(self, question_id):
		#return the question, the answer and the category
		for dic_quest in questions:
			if dic_quest['id'] == question_id:
				question = dic_quest['question']
				answer = dic_quest['answer']
				category = dic_quest['category']
				return {
					'status': '200',
					'question': question,
					'answer': answer,
					'category': category
				}
		return {
			'status': '404'
		}
		
#add to route 'question'
api.add_resource(Questions, '/', '/question/<int:question_id>')

if __name__ == "__main__":
	app.run(debug=True)