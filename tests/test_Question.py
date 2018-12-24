#with pytest

import sys
import pytest
import json
sys.path.append('../app/api')
from Question import Question
import flask_restful
from io import BytesIO

class TestQuestionRequest:
    def simple_question(self):
        return {
            'status':'200',
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
            "level":1
        }
    def mock_path_to_file_question(self):
        return 'question.json'
    def mockread_file(self):
        return [{
            "id":1,
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
            "level":1
            },
            {
            "id":2,
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
            "level":1
            }
        ]
    def test_ResultsShowQuestion(self, monkeypatch, tmpdir):       

        monkeypatch.setattr(Question, 'read_question_file', self.mockread_file)
        question = Question()
        assert question.show_question(1) == self.simple_question()

    def test_ResultsCreateQuestion(self, monkeypatch):
        monkeypatch.setattr(Question, 'path_to_file_question', self.mock_path_to_file_question)
        question = Question()
        assert question.add_question(self.simple_question()) == {'status' : '200 question added'}