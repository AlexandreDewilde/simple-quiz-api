import json
with open('questions.json', 'r') as f:

	print(json.load(f))