import json
from flask_restful import reqparse
import uuid


class Question:

	def path_to_file_question(self):
		"""find the path where is located the questions file"""
		with open('config.txt', 'r') as file:
			path_to_file = file.read()
		return path_to_file
	
	def read_question_file(self):
		"""open and copy the questions file"""
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'r') as json_file:
			questions_json_file = json.load(json_file)
		return questions_json_file

	def write_questions_json_file(self, questions_json_file):
		"""write question json file with the list provided"""
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'w') as file_question:
			json.dump(questions_json_file, file_question)

	def show_question(self, question_id):
		"""return the question according to the question_id provided"""
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
		"""create a question and add it in the json file specified in config.txt"""
		parser = reqparse.RequestParser()
		parser.add_argument('question', type=str, help="the question", required=True)
		parser.add_argument('answer', type=str, required=True, help="the answer")
		
		#category of the questions
		parser.add_argument('category', type=str)

		#int between 1 and 3
		parser.add_argument('level', type=int, help="int between 1 and 3 to define level")
		args = parser.parse_args()

		#check if arg level is between 1 and 3
		try:
			if args['level'] != None: 
				args['level'] = int(args['level'])
				assert args['level'] < 3, "Level must be between 1 and 3"
				assert args['level'] > 1, "Level must be between 1 and 3"
		except AssertionError as error:
			return {
				"error" : str(error)
			}
		except:
			return {
				"error" : "unknow"
			}

		#create dict_element with the args provided in POST and add random id
		keys = ['question', 'answer', 'category', 'level']
		dict_element = {}
		for key in keys:
			dict_element[key] = args[key]
		dict_element['id'] = int(uuid.uuid4())

		#rewrite file with the added question"
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)

		return {
			'status' : '200 question added'
		}

	def delete_question(self):
		"""Delete question with the id provided"""
		parser = reqparse.RequestParser()
		parser.add_argument('id', type=int, required=True)
		args = parser.parse_args()
		questions_json_file = self.read_question_file()
		updated_questions_json_file = []
		for quest in questions_json_file:
			if quest['id'] != args['id']:
				updated_questions_json_file.append(quest)
		self.write_questions_json_file(updated_questions_json_file)
		return {
			'status' : '200, question deleted'
		}
	
	def update_question(self, dic_change):
		"""Update question, answer, ..."""
		pass
	
