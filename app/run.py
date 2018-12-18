import flask
from flask_restful import Resource, Api, reqparse
import json
from api.Questions import *


#create instance of flaskapp = flask.Flask(__name__)
api = Api(app)
		
#add to route 'question'
api.add_resource(Questions, '/', '/question/<int:question_id>')

if __name__ == "__main__":
	app.run(debug=True)