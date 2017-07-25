from flask import url_for

class TestPage(object):

    def test_getall_api(self, client):
        response = client.get(url_for('page.getall'))
        assert response.status_code == 200


    def test_gettree_api(self, client):
        response = client.get("http://localhost/gettree?emp=1000")
        assert response.status_code == 200

    def test_getsubtree_api(self, client):
        response = client.get("http://localhost/getsubtree?emp=1000")
        assert response.status_code == 200

    def test_getsubtree_withjoiningdate_greater_api(self, client):
        response = client.get("http://localhost/getsubtree?emp=1000&&isjdflag=True")
        assert response.status_code == 200

    def test_getshortestpath_api(self, client):
        response = client.get("http://localhost/getshortestpath?emp1=1015&&emp2=1045")
        assert response.status_code == 200



