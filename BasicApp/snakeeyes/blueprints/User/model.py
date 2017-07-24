from snakeeyes.extensions import db
from flask import current_app,jsonify
from lib.util_sqlalchemy import ResourceMixin
from sqlalchemy.exc import IntegrityError
import json


def to_json(result):
    """
    Jsonify the sql alchemy query result.
    """
    res = {}
    ls= []
    for emp in result:
        dc = {}
        if(emp.parent_id == None):
            empId = None
        else:
            empId = int(emp.parent_id)

        if (emp.parent_id == None):
            parId = None
        else:
            parId = int(emp.parent_id)

        dc = {"name" : emp.employee_name,"parentId" : parId,"id" : empId }
        ls.append(dc)
    res={'result':ls}
    return json.dumps(res)


class Employee(db.Model,ResourceMixin):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(60))
    parent_id = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    join_date = db.Column(db.Date)

    def __init__(self,employee_id,employee_name,parent_id,is_active,age,join_date):
        # Call Flask-SQLAlchemy's constructor.
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.parent_id = parent_id
        self.is_active = is_active
        self.age = age
        self.join_date = join_date

    def __init__(self,employee_id,employee_name,parent_id):
        # Call Flask-SQLAlchemy's constructor.
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.parent_id = parent_id

    @classmethod
    def getall(cls):
         current_app.logger.debug('get all api called')
         result = Employee.query.all()
         return to_json(result)

    @classmethod
    def getsubtree(cls):
        result = Employee.filter
        return None

    @classmethod
    def gettree(cls):

        return

    @classmethod
    def getshortesttree(cls):
        return None

    @classmethod
    def setitem(cls,emp):
        e = Employee.query.get(emp.employee_id)
        if(e != None):
            e.employee_name = emp.employee_name
            db.session.commit()
            return jsonify({"status": 201})
        else:
            Employee.save(emp)
            return jsonify({"status":200})

