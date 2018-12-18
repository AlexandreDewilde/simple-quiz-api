import flask
from flask_restful import Resource, Api, reqparse
import json

with open('config.txt', 'r') as file:
	file  = file.read()
with open(file, 'r') as json_file:
	questions_json_file = json.load(json_file)
	
class Questions(Resource):
	
	def get(self, question_id):
		#return the question, the answer and the category
		#open questions.json files
		for dic_quest in questions_json_file:
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