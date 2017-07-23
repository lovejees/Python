from flask import Blueprint, render_template
from snakeeyes.blueprints.User.model import Employee

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/getall',methods=['GET'])
def home():
    return Employee.getall()

