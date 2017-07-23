from snakeeyes.extensions import db
from flask import jsonify

class Employee(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(60))
    parent_id = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    age = db.Column(db.Integer)

    @classmethod
    def getall(cls):

         result = Employee.query.all()
         return jsonify(result)

    @classmethod
    def getsubtree(cls):

        return None

    @classmethod
    def gettree(cls):

        return None

    @classmethod
    def getshortesttree(cls):
        return None

    @classmethod
    def setitem(cls):
        return None