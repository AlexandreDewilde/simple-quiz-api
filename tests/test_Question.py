#with pytest

import sys
import pytest
import json
sys.path.append('../app/api')
from Question import Question
from io import BytesIO

class TestQuestionRequest:
    def test_ResultsShowQuestion(self, monkeypatch):       
        def mockreturn(request):
            return [{
            "id":1,
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
            "level":1
            },
            {
            "id":1,
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
            "level":1
            }
        ]
        reponse = {
            'status':'200',
            "question":"Who is the presidents of USA ?",
            "answer":"Donald Trump",
            "category":"Political",
        }
        monkeypatch.setattr(Question, 'read_question_file', mockreturn)
        question = Question()
        assert question.show_question(1) == reponse