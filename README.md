# Simple-quiz-api
Simple flask app wich run a server with an api implemented
## Features
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
### To show a question with the id provided 
```http://<your_url>/show-question/<id>```  
return json  
### To create a new question
```http://<your_url>/create-question/``` and argument (POST method) question, answer, category, level (int between 1 and 3), it returns json 
## In the next releases
authentification, update question, exception ... 
