from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Todo
from app import db

main_app = Blueprint('main', __name__)


@main_app.route("/")
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@main_app.route("/add", methods=['POST'])
def add_todo():
    title = request.form.get('title')
    new_todo = Todo(text=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))


@main_app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        checked = request.args.get('checked')
        todo.complete = True if checked == 'true' else False
        db.session.commit()
    return redirect(url_for('main.index'))
