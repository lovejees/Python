from flask import Flask
from flask import Flask, jsonify, request,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, Index
from datetime import datetime, timedelta,date
import json

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tiger@localhost:5432/PhoneTool'

app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

db = SQLAlchemy(app)

from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Employee(db.Model,Serializer):
    __tablename__ = 'employee'
    __privacy__ = ('employee_id','employee_name','parent_id','is_active,age')
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(60))
    parent_id = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    age  = db.Column(db.Integer)

    def __repr__(self):
        return '<Employee %r>' % self.age

@app.route('/')
def index():
    """
    Render a Hello World response.

    :return: Flask response
    """
    return app.config['VALUE']


@app.route('/getall',methods = ['GET'])
def getall():
    result = Employee.query.all()
    return jsonify(Employee.serialize_list(result))

@app.route('/tree',methods = ['GET'])
def gettree():
    result = Employee.query.all()
    return jsonify(result)

@app.route('/tree/<jdgflag>',methods = ['GET'])
def subtree():
    result = Employee.query.first()
    return jsonify(result)

@app.route('/shortestpath')
def shortestpath():
    return 'lol'

@app.route('/tree',methods =['POST'])
def settree():
    return 'SetTree'



if __name__ == '__main__':
    db.create_all()
    app.run()