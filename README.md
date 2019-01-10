# Simple quiz api

This repostory is a simple flask app wich run a server with an api implemented.  
The questions are in json files specified in ```config.txt``` (simple question) and ```config_multichoice.txt``` (multiple choice question)
Each question is organize as the example in the next lines:

``` json
{
    "id" : 1,
    "question" : "Who is the president of USA?",
    "answer" : "Donald Trump",
    "category" : "political",
    "level" : 1
}
```

## Features

* Question
* Multiple Choice Question
* JWT token

## Requirements

* [pyton 3.7](https://www.python.org/) and PyPI
* [git](https://git-scm.com/)

## Install

To install:  
Donwload [python 3.7](https://www.python.org/) (add python to path during installation)
Download [git](https://git-scm.com/)

``` bash
git clone https://github.com/allEyezOnCode/simple-quiz-api  
```

In the main folder open a cmd and run:

``` bash
pip install -r requirements.txt
```

## Run app

go in app folder and run in a cmd

``` bash
python run.py
```

or in a Windows powershell

``` powershell
python ./run.py
```

## Usage

## JWT Token

you can change if auth is needed in decorator before each function. You should change the JWT-secret-key  
To get the token:

``` bash
curl -X GET \
  http://<your-url>/auth \
  -H 'Content-Type: application/json' \
  -d '{"username":"test","password":"test"}'
```

it returns

``` bash
{
    "jwt": "<token>"
}
```

### To show all question

``` bash
curl -X GET \
  http://<your-url>/show-all-question \
```

### To show all simple-question-categories
```bash
curl -X GET \
 http://<your-url>/show-all-categories \

### To show a question with the id provided

``` bash
curl -X GET \
  http://127.0.0.1:5000/show-question/1 \
```

### To create a new question

``` bash
curl -X POST \
  http://127.0.0.1:5000/add-question \
  
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <your token>' \
  -d '{
    "question":"<your-question>",
    "answer":"<your answer>",
    "level":<int btw 1 and 3>,
    "category":"<your-category>"
}'
```

It returns json, if the question added:

``` json
"status" : "200 question added"
```

### To delete a question

``` bash
curl -X POST \
  http://127.0.0.1:5000/delete-question \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <your token>' \
  
  -d '{
    "id":<int between 1 and 3>
}'
```

### To add multiple choice question

``` bash
curl -X POST \
  http://127.0.0.1:5000/add_multiple-choice-question \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <your token>' \
  -d '{
    "question":"<your-question>",
    "answer":"<your answer>",
    "choice":"[<choice 1>, <choice2>, <choice3>, <choice4>]",
    "level":1,
    "category":"<your-category>"
}'
```

### Show all, show all categories, show and delete multiple choice question

Same for simple question but the url is for

* del /delete-multiple-choice-question
* show all /show-all-multiple-choice-question
* show /show-multiple-choice-question
* show all categories /show-all-categories-multichoice

## In the next releases

Tests

## Contributing

Feel free to contribute, fork repo add your changes and submit a Pull request
