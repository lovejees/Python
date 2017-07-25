from snakeeyes.extensions import db
from lib.util_sqlalchemy import ResourceMixin
from lib.util import Utils
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
import json
from flask import jsonify

"""


def to_json(result):
    
    Jsonify the sql alchemy query result.
    
    res = {}
    ls= []
    for emp in result:
        dc = {}
        if(emp.employee_id == None):
            empId = None
        else:
            empId = int(emp.employee_id)

        if (emp.parent_id == None):
            parId = None
        else:
            parId = int(emp.parent_id)

        dc = {"name" : emp.employee_name,"parentId" : parId,"id" : empId }
        ls.append(dc)
    res={'result':ls}
    return json.dumps(res)
"""

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
       #  current_app.logger.debug('get all api called')
         result = Employee.query.all()
         return Utils.todict(result)

    @classmethod
    def getsubtree(cls,empId,isjoindateflag):
        sql =  text("WITH RECURSIVE subordinates AS "+
         "(SELECT employee_id,parent_id,employee_name,join_date FROM employee WHERE employee_id = :id"
         " UNION SELECT e.employee_id, e.parent_id, e.employee_name,e.join_date FROM employee e "+
         "INNER JOIN subordinates s ON s.employee_id = e.parent_id) SELECT employee_name,parent_id,employee_id  FROM subordinates"+
                    " where employee_id <> :id")
        if(isjoindateflag == True):
            sql = text("WITH RECURSIVE subordinates AS "+
         "(SELECT employee_id,parent_id,employee_name,join_date FROM employee WHERE employee_id = :id"
         " UNION SELECT e.employee_id, e.parent_id, e.employee_name,e.join_date FROM employee e "+
         "INNER JOIN subordinates s ON s.employee_id = e.parent_id) SELECT employee_name,parent_id,employee_id  FROM subordinates"+
                    " where employee_id <> :id  and join_date > (select join_date from employee where employee_id = :id)")


        result = db.session.query(Employee).from_statement(sql).params(id=empId).all()
        return Utils.todict(result)

    @classmethod
    def gettree(cls,empId):
        sql =  text("WITH RECURSIVE subordinates AS "+
             "(SELECT employee_id,parent_id,employee_name,join_date FROM employee WHERE employee_id = :id"
             " UNION SELECT e.employee_id, e.parent_id, e.employee_name,e.join_date FROM employee e "+
             "INNER JOIN subordinates s ON s.employee_id = e.parent_id) SELECT employee_name,parent_id,employee_id  FROM subordinates")

        result = db.session.query(Employee).from_statement(sql).params(id=empId).all()
        return Utils.todict(result)


    @classmethod
    def getancestorpath(cls,empId):
        sql = text("WITH RECURSIVE subordinates AS "+
                   "(SELECT employee_id,parent_id,employee_name,join_date FROM employee WHERE employee_id = :id "+
                   "UNION SELECT e.employee_id, e.parent_id, e.employee_name,e.join_date FROM employee e INNER JOIN "+
                   "subordinates s ON s.parent_id = e.employee_id)SELECT employee_name,parent_id,employee_id,join_date FROM subordinates")

        result = db.session.query(Employee).from_statement(sql).params(id=empId).all()
        return result

    @classmethod
    def setitem(cls,emp):
        e = Employee.query.get(emp.employee_id)
        if(e != None):
            e.employee_name = emp.employee_name
            e.id = emp.id
            e.parent_id = emp.parent_id
            db.session.commit()
            return json.dumps({"status": "insert successful"})
        else:
            Employee.save(emp)
            return json.dumps({"status": "update successful"})

    @classmethod
    def delitem(cls,employee_id):
        e = Employee.query.get(employee_id)
        if(e != None):
            try:
                Employee.delete(e)
            except Exception :
                return jsonify({"status" : "failed"})
        return jsonify({"status": "success"})


