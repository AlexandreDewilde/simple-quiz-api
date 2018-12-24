import json
import uuid


class Question:

	def path_to_file_question(self):
		"""find the path where is located the questions file"""
		with open('config.json', 'r') as file:
			file = json.load(file)
		return file["simple_question_path"]
	
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
		#open and read json file
		question_file = self.read_question_file()

		#find question in the json file
		for dic_quest in question_file:
			if dic_quest['id'] == question_id:
				return {
					'status': '200',
					'question': dic_quest['question'],
					'answer': dic_quest['answer'],
					'category':dic_quest['category'],
					'level': dic_quest['level']
				}

		#if the id is not in the json it returns 404
		return {
			'status': '404'
		}

	def show_all_question(self):
		return self.read_question_file()

	def add_question(self, dict_element):
		"rewrite file with the added question and args"
		#generate id
		dict_element['id'] = int(uuid.uuid4())

		#open, read and write the new question in json file
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)

		return {
			'status' : '200 question added'
		}

	def delete_question(self, id):
		"""Delete question with the id provided"""
		#read json file
		questions_json_file = self.read_question_file()

		#create a new list with the question deleted
		updated_questions_json_file = []
		for quest in questions_json_file:
			if quest['id'] != id:
				updated_questions_json_file.append(quest)
		self.write_questions_json_file(updated_questions_json_file)

		#returns OK
		return {
			'status' : '200, question deleted'
		}

	#in the next releases
	def update_question(self, dic_change):
		"""Update question, answer, ..."""
		pass
	
