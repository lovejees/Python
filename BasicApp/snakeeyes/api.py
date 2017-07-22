from snakeeyes.app import app
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tiger@localhost:5432/PhoneTool'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


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

