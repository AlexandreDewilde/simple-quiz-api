# Simple-quiz-api
Simple flask app wich run a server with an api implemented
## Features
* JWT authentification 
* Multiple choice question
* Simple Choice Question
## Requirements
* [pyton 3.6](https://www.python.org/) and pip
* [git](https://git-scm.com/) 

## Installation
To install open git bash and clone the repository  
```git clone https://github.com/allEyezOnCode/simple-quiz-api```  
In the repository open bash and run:   
```pip install -r requirements.txt```
## Start Server
go in app folder and run in a cmd   
```python run.py```
## Usage
### To show a question with the id provided (Require no auth) 
```http://<your_url>/show-question/<id>```  
return json  
### To create a new question
```$ curl -X POST http://localhost:5000/create-question/ -H "Authorization: JWT <your token> -d "question=<question>" -d "answer=<answer>" -d "level=<>" -d "category=<>"``` and argument (POST method) question, answer, category, level (int between 1 and 3), it returns json 
## In the next releases
authentification, update question, exception ... 
