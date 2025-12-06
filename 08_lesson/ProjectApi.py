import requests
from config import Config

class ProjectApi():
    def __init__(self):
        self.base_url = f"{Config.API_URL}/projects"
        self.headers = Config.HEADERS
        self.project_id = None
        
#Создать проект        
    def create_project(self, title = 'ГосУслуги'):
        project = {
            'title': title
        }
        resp = requests.post(self.base_url, json = project, headers = self.headers)
        result = resp.json()
        self.project_id = result.get('id')
        return resp
    
#Изменить проект
    def update_project(self, new_title = 'УслугиГОСсектора'):
        project = {
            'title': new_title
        }
        resp = requests.put(self.base_url + f'/{self.project_id}', json = project,
                            headers = self.headers)
        result = resp.json()
        self.project_update_id = result.get('id')
        return resp
    
#Получить по ID
    def get_project_by_ID(self):
        resp = requests.get(self.base_url + f'/{self.project_id}',
                            headers = self.headers)
        return resp

        
