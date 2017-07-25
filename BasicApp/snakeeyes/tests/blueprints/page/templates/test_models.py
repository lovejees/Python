#import mock
import pytest
from pytest_mock import mocker
from snakeeyes.blueprints.User.model import Employee


def test_update_jobs_fleet_capacity(mocker):
    mocker.patch.object(Employee, 'getall')
    Employee.getall.return_value = 120
    result = Employee.getall()
    print(result)