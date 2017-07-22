from snakeeyes.app import flaskapp
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tiger@localhost:5432/PhoneTool'
flaskapp.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(flaskapp)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    status = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@flaskapp.route('/l')
def show_all():
    return render_template('show_all.html', students=Todo.query.all())


@flaskapp.route('/newl', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = Todo(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    flaskapp.run(debug=True)