from flask import Flask
from flask_cors import CORS

from src.repositorio import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hola mundo desde Peñascal"

@app.route('/tasks', methods=['GET'])
def all_tasks():
    return get_tasks()

@app.route('/tasks', methods=['POST'])
def new_task():
     create_task()
     return "Tarea agregada correctamente"

@app.route('/tasks/<int:task_id>', methods=['GET'])
def task(task_id):
    return get_task(task_id)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_tarea(task_id):
    update_task(task_id)
    #return "Tarea actualizada correctamente"
    return ""

 
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_tarea(task_id):
      delete_task(task_id) 
      return f"La tarea {task_id} ha sido borrada"

if __name__ == "__main__":
    app.run(debug=True)