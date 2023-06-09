from flask import Flask, request
from flask_cors import CORS

from src.repository import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, world. Everything ok"


#1
@app.route("/tasks", methods=["GET"])
def all_tasks():
    return get_tasks()

#2
@app.route('/tasks', methods=['POST'])
def new_task():
    data = request.get_json()
    create_task(data)
    return ""

#3
@app.route('/tasks/<int:task_id>', methods=['GET'])
def task(task_id):
    return get_task(task_id)

#4
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    update_task(task_id, data)
    return ""

#5
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
      delete_task(task_id) 
      return ""


if __name__ == "__main__":
    app.run(debug=True)