from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {
        "id": 1,
        "text": "This is a todo 1"
    },
    {
        "id": 2,
        "text": "This is a todo 2"
    },
    {
        "id": 3,
        "text": "This is a todo 3"
    }
]
id_counter = 3


@app.route('/')
def index():
    return render_template("index.html", todos=todos)


@app.route('/remove')
def remove():
    todo_id = request.args.get('todo_id')
    for todo in todos:
        if todo['id'] == int(todo_id):
            todos.remove(todo)
            break
    return redirect("/")


@app.route('/add')
def add():
    new_todo_text = request.args.get('todo-text')
    global id_counter
    global todos
    id_counter+=1
    todos.append({"id":id_counter, "text":new_todo_text})
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
