from flask import Flask
from flask import Flask, jsonify, request,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, Index
from datetime import datetime, timedelta
import json

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tiger@localhost:5432/PhoneTool'

app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

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
        self.status = False
        self.pub_date = datetime.utcnow()

@app.route('/')
def index():
    """
    Render a Hello World response.

    :return: Flask response
    """
    return app.config['VALUE']


@app.route('/getall',methods = ['GET'])
def getall():
    result = Todo.query.first()
    return jsonify(result.as_dict())

@app.route('/new',methods =['POST'])
def addnew():
    if not request.json or not 'name' in request.json:
        abort(400)
    todo = Todo(request.json.name, request.json.get('hireDate', ''), request.json.get('focus', ''))
    db.session.add(todo)
    db.session.commit()
    return jsonify({'developer': todo}), 201



if __name__ == '__main__':
    db.create_all()
    app.run()