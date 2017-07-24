from flask import Blueprint, render_template ,request
from snakeeyes.blueprints.User.model import Employee

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/getall',methods=['GET'])
def getall():
    return Employee.getall()

@page.route('/gettree',methods=['GET'])
def gettree():
    return Employee.gettree()

@page.route('/getsubtree',methods=['GET'])
def getsubtree():
    return Employee.getsubtree()

@page.route('/getshortestpath',methods=['GET'])
def getshortestpath():
    return Employee.getshortesttree()

@page.route('/settree',methods=['POST'])
def settree():
    parentId = request.json['parentId']
    name = request.json['name']
    id = request.json['id']
    emp = Employee(id,name,parentId)
    return Employee.setitem(emp)

