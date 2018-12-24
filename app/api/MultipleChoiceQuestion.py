from api.Question import Question
from flask_restful import reqparse
import uuid
import json


class MultipleChoiceQuestion(Question):
	def path_to_file_question(self):
		#find the path where is located the questions file
		with open('config.json', 'r') as file:
			file = json.load(file)
		return file["multiple_choice_question_path"]

	def show_question(self, question_id):
		"""return the question according to the question_id provided"""
		#open and read json file
		question_file = self.read_question_file()

		#find question in the json file
		for dic_quest in question_file:
			if dic_quest['id'] == question_id:
				return {
					'status': '200',
					'question': dic_quest['question'],
					'choice': dic_quest['choice'],
					'answer': dic_quest['answer'],
					'category':dic_quest['category'],
					'level': dic_quest['level']
				}

		#if the id is not in the json it returns 404
		return {
			'status': '404'
		}
