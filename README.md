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

### To show a question with the id provided

``` bash
curl -X GET http://<your_url>/show-question/<int:id>
```

### To create a new question

``` bash
curl -X POST http://<url>/add-question/ -d "question=<question>" -d "answer=<answer>" -d "level=<int btw 1 and 3>" -d "category=<category>"
```

It returns json, if the question added:

``` json
"status" : "200 question added"
```

### To delete a question

``` bash
curl -X POST http://<url>/delete-question/ -d "id=<id>"
```

### For mulitiple choice

It's the same except you have one extra argument "choice" it's a list of string and the url are a bit different add "multiple-choice" by instance : "add-multiple-choice-question" or "delete-multiple-choice-question"

## In the next releases

Show all questions, Oauth, tests, update a question, ...
