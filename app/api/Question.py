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
		
		#check if required args are in dict_element
		for key in ["question", "answer"]:
			if key not in dict_element:
				return {
					'status': f"{key} is required"
				}

		#check if args and exists and if not add None
		for key in ["level", "category"]:
			if key not in dict_element:
				dict_element[key] = None

		#check if level is between 1 and 3
		if dict_element["level"] != None and dict_element["level"] > 3 or dict_element["level"] < 1:
			return {
				"status":"Error level must be between 1 and 3"
			}
		#open, read and write the new question in json file
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)

		return {
			'status' : '200 question added'
		}

	def delete_question(self, question_id):
		"""Delete question with the id provided"""
		#read json file
		questions_json_file = self.read_question_file()
		delete_bool = False

		#create a new list with the question deleted
		updated_questions_json_file = []
		for quest in questions_json_file:
			if quest['id'] != question_id:
				updated_questions_json_file.append(quest)
			else:
				delete_bool = True

		if not delete_bool:
			return {"status": "Error id doesn't exist"}

		self.write_questions_json_file(updated_questions_json_file)

		#returns OK
		return {
			"status" : "200, question deleted"
		}

	#in the next releases
	def update_question(self, dic_change):
		"""Update question, answer, ..."""
		try:
			if id not in dic_change:
				raise AssertionError()
			keys =  ["category", "level", "question", "answer", "choice"]
			updated_list = []
			for dic in self.read_question_file():
				if dic["id"] == dic_change["id"]:
					for key in keys:
						if key in dic_change:
							dic[key] = dic_change[key]
				updated_list.append(dic)
		except AssertionError as assert_error:
			return {
				"status": f"error : {assert_error}"
			}
		self.write_questions_json_file(updated_list)
		return {
			"status":"200 question updated"
		}


	
