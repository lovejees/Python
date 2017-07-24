from flask import Blueprint, render_template ,request,json
from snakeeyes.blueprints.User.model import Employee
import networkx as nx

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/getall',methods=['GET'])
def getall():
    return Employee.getall()

@page.route('/gettree',methods=['GET'])
def gettree():
    return Employee.gettree(request.args.get('employeeId'))

@page.route('/getsubtree',methods=['GET'])
def getsubtree():
    isjoindateflag = request.args.get('isjdflag')

    return Employee.getsubtree(request.args.get('employeeId'),isjoindateflag)

@page.route('/getshortestpath',methods=['GET'])
def getshortestpath():
    src = int(request.args.get('emp1'))
    des = int(request.args.get('emp2'))

    list1 = Employee.getancestorpath(src)
    list2 = Employee.getancestorpath(des)

    shortpath = getshortpath(list1,list2,src,des)
    return json.dumps(shortpath)

@page.route('/settree',methods=['POST'])
def settree():
    parentId = request.json['parentId']
    name = request.json['name']
    id = request.json['id']
    emp = Employee(id,name,parentId)
    return Employee.setitem(emp)

def getshortpath(list1,list2,src,des):
    G = nx.Graph()

    addtograph(list1,G)
    addtograph(list2,G)

    return nx.shortest_path(G,source=src,target=des)

def addtograph(list,G):
    for emp in list:
        if(emp.employee_id != None) and (emp.parent_id != None):
            G.add_edge(int(emp.employee_id),int(emp.parent_id))
    return None