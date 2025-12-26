import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
task = []

def test_create_task():
    new_task = {
    "title":"admin2",
    "description":"descrição de teste"
    }
    reponse = requests.post(f"{BASE_URL}/tasks", json=new_task)

    assert reponse.status_code ==201
