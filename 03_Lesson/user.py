class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def name(self):
        print(self.first_name)
    def suname(self):
        print(self.last_name)
    def name_and_suname(self):
        print(f'{self.first_name} {self.last_name}')