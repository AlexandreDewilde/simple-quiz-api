from . Question import Question
from flask_restful import reqparse
import uuid
import json


class MultipleChoiceQuestion(Question):
	def path_to_file_question(self):
		#find the path where is located the questions file
		with open('config_multichoice.txt', 'r') as file:
			path_to_file = file.read()
		return path_to_file

	def show_question(self, question_id):
		#return the question according to the question_id provided
		question_file = self.read_question_file()
		for dic_quest in question_file:
			if dic_quest['id'] == question_id:
				return {
					'status': '200',
					'question': dic_quest['question'],
					'choice' :  dic_quest['choice'],
				 	'answer': dic_quest['answer'],
					'category': dic_quest['category']
				}
		return {
			'status': '404'
		}

	def create_question(self):
		"""create a question and add it in the json file specified in config_mutiplechoice.txt"""
		parser = reqparse.RequestParser()
		parser.add_argument('question', type=str, help="the question", required=True)
		parser.add_argument('choice', action='append', help="choice for the question", required=True)
		parser.add_argument('answer', type=str, required=True, help="the answer")
		
		#category of the questions
		parser.add_argument('category', type=str)

		#int between 1 and 3
		parser.add_argument('level', type=int, help="int between 1 and 3 to define level")
		args = parser.parse_args()

		#check if  arg level is between 1 and 3
		try:
			if args['level'] != None: assert args['level'] < 3, "Level must be between 1 and 3"
		except AssertionError as error:
			return {
				"error" : str(error)
			}

		#converts args object to a dict 
		keys = ['question', 'choice', 'answer', 'category', 'level']
		dict_element = {}
		dict_element['id'] = int(uuid.uuid4())
		for key in keys:
			dict_element[key] = args[key]
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)
		return {
			'status' : '200 question added'
		}