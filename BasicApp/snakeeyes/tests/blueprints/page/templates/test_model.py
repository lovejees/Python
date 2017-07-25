from flask import json
from snakeeyes.blueprints.User.model import Employee
from lib.tests import assert_result_is_dictionary
DUMMY_ID = 1000

class TestModel():


    def test_getall(self,client):
        result = Employee.getall()
        assert_result_is_dictionary(result,dict)

    def test_gettree(self,client):
        result = Employee.gettree(DUMMY_ID)
        assert_result_is_dictionary(result,dict)

    def test_getsubtree_joiningdateflag_notset(self,client):
        result = Employee.getsubtree(DUMMY_ID,False)
        assert_result_is_dictionary(result,dict)

    def test_getsubtree_joiningdateflag_set(self,client):
        result = Employee.getsubtree(DUMMY_ID,True)
        assert_result_is_dictionary(result,dict)

    def test_getancestorpath(self,client):
        result = Employee.getancestorpath(DUMMY_ID)
        assert_result_is_dictionary(result,list)





