import flask
from flask_restful import Api
from api.OperationQuestion import *

#create instance of flask
app = flask.Flask(__name__)
api = Api(app)

#add to route the classes for simple question
api.add_resource(ShowQuestion, '/', '/show-question/<int:question_id>')
api.add_resource(CreateQuestion, '/', '/add-question/')
api.add_resource(DeleteQuestion, '/', '/delete-question/')

#add to route classes for mutilple choice question
api.add_resource(CreateMultipleChoiceQuestion, '/', '/add-multi-choice-question/')
api.add_resource(ShowMultipleChoiceQuestion, '/show-multiple-choice-question/<int:question_id>')
api.add_resource(DeleteMultipleChoiceQuestion, '/', '/delete-multi-choice-question/')

if __name__ == "__main__":
	app.run(debug=True)