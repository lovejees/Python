from snakeeyes.extensions import db
from flask import current_app
from lib.util_sqlalchemy import ResourceMixin
import json


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

class Employee(db.Model,ResourceMixin):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(60))
    parent_id = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    age = db.Column(db.Integer)

    def __init__(self,employee_id,employee_name,parent_id,is_active,age):
        # Call Flask-SQLAlchemy's constructor.
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.parent_id = parent_id
        self.is_active = is_active
        self.age = age

    @classmethod
    def getall(cls):

         current_app.logger.debug('log message')
         result = Employee.query.all()
         return 'LoL'

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