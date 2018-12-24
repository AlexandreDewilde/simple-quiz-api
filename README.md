# Simple quiz api

This repostory is a simple flask app wich run a server with an api implemented. Contrib are open
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

### To show all question

``` bash
curl -X GET \
  http://<your-url>/show-all-question \
```

### To show a question with the id provided

``` bash
curl -X GET \
  http://127.0.0.1:5000/show-question/1 \
```

### To create a new question

``` bash
curl -X POST \
  http://127.0.0.1:5000/add-question \
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
  -d '{
    "id":<int between 1 and 3>
}'
```

### To add multiple choice question

``` bash
curl -X POST \
  http://127.0.0.1:5000/add_multiple-choice-question \
  -H 'Postman-Token: 10d64671-f6e0-4ddd-aa88-f52ab0501d10' \
  -H 'cache-control: no-cache' \
  -d '{
    "question":"<your-question>",
    "answer":"<your answer>",
    "choice":"[<choice 1>, <choice2>, <choice3>, <choice4>]",
    "level":1,
    "category":"<your-category>"
}'
```

### Show all, show and delete multiple choice question

Same for simple question but the url is for

* del /delete-multiple-choice-question
* show all /show-all-multiple-choice-question
* show /show-multiple-choice-question

## In the next releases

Show all questions, Oauth, tests, update a question, ...
