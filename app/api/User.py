import json
from flask_jwt import JWT, jwt_required
import sys

USER_DATA = {"admin": "admin"}

class User:
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        return f"User(id={self.id})"

def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=1)
        
def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

