from ProjectApi import ProjectApi
import pytest

@pytest.fixture
def project_api():
    return ProjectApi()

def test_create_project(project_api):
        resp = project_api.create_project()
        print(f"Статус созданного проекта: {resp.status_code}")
        print(f"Текст проекта: {resp.text}")
        assert resp.status_code == 201
        project = resp.json()
        assert 'id' in project
        assert project['id'] is not None

def test_create_project_negative(project_api):
        resp = project_api.create_project(title = None)
        print(f"Статус созданного проекта: {resp.status_code}")
        assert resp.status_code == 400
        
def test_update_project(project_api):
        project_api.create_project()
        resp = project_api.update_project()
        print(f"Статус созданного проекта: {resp.status_code}")
        print(f"Текст проекта: {resp.text}")
        assert resp.status_code == 200
        new_id = resp.json()
        assert 'id' in new_id
        assert new_id['id'] is not None
        
def test_update_project_negative(project_api):
        resp = project_api.update_project()
        print(f"Статус созданного проекта: {resp.status_code}")
        assert resp.status_code == 404
        
def test_get_by_ID(project_api):
        project_api.create_project()
        resp = project_api.get_project_by_ID()
        print(f"Статус запроса: {resp.status_code}")
        print(f"Текст запроса: {resp.text}")
        assert resp.status_code == 200
        project = resp.json()
        assert project['title'] == 'ГосУслуги'
        
def test_get_by_ID_negative(project_api):
        resp = project_api.get_project_by_ID()
        print(f"Статус запроса: {resp.status_code}")
        assert resp.status_code == 404
        