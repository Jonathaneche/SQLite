from flask import request, jsonify
import sqlite3


# Configuración de la base de datos
DB_NAME = 'tasks.db'


# Crea la tabla 'tasks' en la base de datos si no existe
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0)''')
conn.commit()
conn.close()

def get_db_connection():
    # Establece una conexión a la base de datos SQLite
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def get_tasks():
    # Obtiene todas las tareas de la base de datos 
    # y las devuelve en formato JSON
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    task_list = [dict(task) for task in tasks]
    return jsonify(task_list)

def create_task():
    # Crea una nueva tarea y la guarda en la base de datos
    data = request.json
    title = data['title']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()
    new_task_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.close()
    new_task = {'id': new_task_id, 'title': title, 'completed': 0}
    return jsonify(new_task), 201

def get_task(task_id):
    # Obtiene una tarea específica según el ID proporcionado
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    if task:
        return jsonify(dict(task))
    return jsonify({'error': 'Task not found'}), 404

#Esta función recoge la data que viene del Front

def update_task(task_id):
    # Actualiza una tarea existente según el ID proporcionado
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        title = request.json.get('title', task['title'])
        completed = request.json.get('completed', task['completed'])
        conn.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?',
                    (title, completed, task_id))
        conn.commit()
        conn.close()
        updated_task = {'id': task_id, 'title': title, 'completed': completed}
        return jsonify(updated_task)
    return jsonify({'error': 'Task not found'}), 404

def delete_task(task_id):
    # Elimina una tarea existente según el ID proporcionado
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404
