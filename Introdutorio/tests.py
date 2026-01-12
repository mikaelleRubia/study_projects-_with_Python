import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task = {
    "title":"admin2",
    "description":"descrição de teste"
    }
    reponse = requests.post(f"{BASE_URL}/tasks", json=new_task)
    result = reponse.json()

    assert reponse.status_code ==201
    assert 'id' in result["task"]
    tasks.append(result["task"]['id'])


def test_get_tasks():
    reponse = requests.get(f"{BASE_URL}/tasks")
    result = reponse.json()

    assert reponse.status_code ==200
    assert 'Tasks' in result
    assert isinstance(result['Tasks'], list)

