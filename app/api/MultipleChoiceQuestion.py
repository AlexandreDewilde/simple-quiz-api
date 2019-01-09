from api.Question import Question
import json


class MultipleChoiceQuestion(Question):

	def path_to_file_question(self):
		#find the path where is located the questions file
		with open('config.json', 'r') as file:
			file = json.load(file)
		return file["multiple_choice_question_path"]

	def read_question_file(self):
		"""open and copy the questions file"""
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'r') as json_file:
			questions_json_file = json.load(json_file)
		return questions_json_file


	def show_categories(self):
		"""return all the categories of questions and the number of questions each one has
		,not the null categories of course"""
		#open and read json file
		json_file = self.read_question_file()
		categories = {}
		categories_num = {}
		i = 0

		#find categories in the json file and insert them in a dictionary with seperate keys
		for category in json_file:
			cat = category['category']
			if not(cat is None):
				if not(cat in categories.values()): #check for duplicate categories
					key = "category " + str(i + 1)
					categories[key] = cat
					i = i + 1
					categories_num[cat] = 1
				else:
					if (cat in categories_num):
						categories_num[cat] = categories_num[cat] + 1

		#create a dictionary with nested values
		data = {}
		for item in categories:
			category = categories[item]
			data[category] = {}
			data[category]['number of questions'] =  categories_num[category]

		if categories:
			return{
			"categories" : 	data
			}
		else:
			#in case all the categories are null it returns special message
			return{
			"status" : "No categories have been created"
			}

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
