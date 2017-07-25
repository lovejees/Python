from flask import Blueprint,request,jsonify
from snakeeyes.blueprints.User.model import Employee
from lib.graphutil import GraphUtil

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/getall',methods=['GET'])
def getall():
        return jsonify(Employee.getall())

@page.route('/gettree',methods=['GET'])
def gettree():
    return jsonify(Employee.gettree(request.args.get('emp')))

@page.route('/getsubtree',methods=['GET'])
def getsubtree():
    isjoindateflag = request.args.get('isjdflag')
    return jsonify(Employee.getsubtree(request.args.get('id'),isjoindateflag))

@page.route('/getshortestpath',methods=['GET'])
def getshortestpath():
    src = int(request.args.get('emp1'))
    des = int(request.args.get('emp2'))

    list1 = Employee.getancestorpath(src)
    list2 = Employee.getancestorpath(des)

    shortpath = GraphUtil.shortestpath(list1,list2,src,des)
    return jsonify(shortpath)

@page.route('/settree',methods=['POST'])
def settree():
    parentId = request.json['parent_id']
    name = request.json['employee_name']
    id = request.json['employee_id']
    emp = Employee(id,name,parentId)

    return Employee.setitem(emp)


@page.route('/delnode',methods=['GET'])
def delnode():
    id = request.args.get('emp')
    return Employee.delitem(id)