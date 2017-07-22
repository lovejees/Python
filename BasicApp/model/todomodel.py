"""


from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from snakeeyes.app import flaskapp

flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
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

if __name__ == '__main__':
    db.create_all()

"""
