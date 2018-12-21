import flask
from flask_restful import Api
from api.ShowQuestion import ShowQuestion
from api.CreateQuestion import CreateQuestion
from api.DeleteQuestion import DeleteQuestion


#create instance of flask
app = flask.Flask(__name__)
api = Api(app)
		
#add to route the class
api.add_resource(ShowQuestion,  '/show-question/<int:question_id>')
api.add_resource(CreateQuestion, '/add-question/')
api.add_resource(DeleteQuestion, '/delete-question/')
if __name__ == "__main__":
	app.run(debug=True)