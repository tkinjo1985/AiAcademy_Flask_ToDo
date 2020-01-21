import functools
from datetime import datetime as dt

from flask import Blueprint, redirect, render_template, request, url_for

from todo.db import get_db

bp = Blueprint('todo', __name__, url_prefix='/')

date = dt.now().strftime('%Y:%m:%d %H:%I:%S')


def get_all_tasks():
    db = get_db()
    tasks = db.execute(
        'SELECT task_id,task_content,done_flag,created_at FROM todo WHERE done_flag = 0'
    ).fetchall()

    return tasks


def get_all_done_tasks():
    db = get_db()
    tasks = db.execute(
        'SELECT task_id,task_content,done_flag,created_at FROM todo WHERE done_flag = 1'
    ).fetchall()

    return tasks


@bp.route('/', methods=('GET',))
def index():
    # タスクリストを取得
    tasks = get_all_tasks()
    done_tasks = get_all_done_tasks()

    # index.htmlにはリストを渡す
    return render_template('index.html', tasks=list(tasks), done_tasks=list(done_tasks))


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        content = request.form['content']
        error = None

        if not content:
            error = 'Content is required.'

        if error is None:
            db = get_db()
            db.execute('insert into todo(task_content,done_flag,created_at) values(?, ?, ?)',
                       (request.form['content'], 0, date))
            db.commit()
            return redirect(url_for('todo.index'))


@bp.route('/done', methods=('POST',))
def done():
    db = get_db()
    db.execute('UPDATE todo SET done_flag=1 where task_id=?',
               (request.form['task_id'], ))
    db.commit()
    return redirect(url_for('todo.index'))


@bp.route('/update', methods=('POST',))
def update():
    db = get_db()
    db.execute(
        'UPDATE todo SET task_content=? where task_id=?', (
            request.form['content'], request.form['task_id'])
    )
    db.commit()
    return redirect(url_for('todo.index'))
