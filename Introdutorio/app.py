from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models.task import Task


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
CORS(app)



tasks = []
task_control=0


@app.route('/tasks', methods=["POST"])
def create_tasks(): 
    global task_control

    data = request.get_json()
    task = Task(id=task_control, title=data.get("title"), description=data.get("description", ""))
    task_control += 1
    tasks.append(task)
    return jsonify({
        "message":"Teste",
        "task": task.to_dict(),
        "task_control":task_control
        }),201

@app.route('/tasks', methods=["GET"])
def get_tasks():
    if len(tasks) == 0:
        return jsonify({"message": "Nenhuma task cadastrada"}), 404
    else:
        tasks_data = []
        for task in tasks:
            tasks_data.append(task.to_dict())
        return jsonify({"Tasks": tasks_data})


if __name__ == "__main__":
    app.run(debug=True)

