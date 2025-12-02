import requests

class ProjectApi():
    def __init__(self, url):
        self.url = url
        self.company_id = None
        self.token = None
        self.project_id = None
        self.new_project_id = None
        
#Получить ID компании
    def get_company_id(self, login = 'natnata0897@gmail.com', password = 'Yatakhochu', name = '108.1'):
        creds = {
            'login': login,
            'password': password,
            'name': name     
        }
        resp = requests.post(self.url + '/auth/companies', json = creds)
        result = resp.json()
        company_id = result['content'][0]['id']
        self.company_id = company_id
        return {'id': company_id} 
    
# Получить токен авторизации
    def get_token(self, login = 'natnata0897@gmail.com', password = 'Yatakhochu'):
        creds = {
            'login': login,
            'password': password,
            'companyId': self.company_id  
        }
        resp = requests.post(self.url + '/auth/keys', json = creds)
        result = resp.json()
        self.token = result.get('key')
        return result
        
    
#Создать проект
    def create_project(self, title = 'ГосУслуги'):
        project = {
            'title': title
        }
        resp = requests.post(self.url + '/projects', json = project)
        result = resp.json()
        self.project_id = result.get('id')
        return result
    
#Негативный
    def create_project_negative(self, title = None):
        project = {
            'title': title
        }
        resp = requests.post(self.url + '/projects', json = project)
        print(resp)
    
#Изменить проект
    def update_project(self, new_title = 'УслугиГОСсектора'):
        project = {
            'new_title': new_title
        }
        resp = requests.put(self.url + f'/projects/{self.project_id}', json = project)
        result = resp.json()
        self.new_project_id = result.get('id')
        return result
    
#Изменить проект негативный
    def update_project_negative(self, new_title = 'Услуги'):
        project = {
            'new_title': new_title
        }
        resp = requests.put(self.url + f'/projects/{None}', json = project)
        result = resp.json()
        self.new_project_id = result.get('id')
        return result
    
#Получить по ID
    def get_project_by_ID(self):
        resp = requests.get(self.url + f'/projects/{self.project_id}')
        return resp.json()
        

#Получить по ID негативный
    def get_project_by_ID_negative(self):
        resp = requests.get(self.url + f'/projects')
        return resp.json()
        
        
        
    