import json
from flask_restful import reqparse
import uuid


class Question:

	def path_to_file_question(self):
		#find the path where is located the questions file
		with open('config.txt', 'r') as file:
			path_to_file = file.read()
		return path_to_file
	
	def read_question_file(self):
		#open and copy the questions file
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'r') as json_file:
			questions_json_file = json.load(json_file)
		return questions_json_file

	def write_questions_json_file(self, questions_json_file):
		#write question json file with the object provided
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'w') as file_question:
			json.dump(questions_json_file, file_question)

	def show_question(self, question_id):
		#return the question according to the question_id provided
		question_file = self.read_question_file()
		for dic_quest in question_file:
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
	
	def create_question(self):
		parser = reqparse.RequestParser()
		parser.add_argument('question', type=str, help="the question", required=True)
		parser.add_argument('answer', type=str, required=True, help="the answer")
		#category of the questions
		parser.add_argument('category', type=str)
		#int between 1 and 3 to define args
		parser.add_argument('level', type=int, help="int between 1 and 3 to define level")
		args = parser.parse_args()
		#converts args object to a dict 
		keys = ['question', 'answer', 'category', 'level']
		dict_element = {}
		for nb_plus_1, key in enumerate(keys):
			dict_element[keys[nb_plus_1 - 1]] = args[key]
		dict_element['id'] = int(uuid.uuid4())
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)
		return {
			'status' : '200 question added'
		}

	def delete_question(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id', type=int, required=True)
		args = parser.parse_args()
		questions_json_file = self.read_question_file()
		update_questions_json_file = []
		for quest in questions_json_file:
			if quest['id'] != args['id']:
				update_questions_json_file.append(quest)
		self.write_questions_json_file(update_questions_json_file)
		return {
			'status' : '200, question deleted'
		}