class Student:
    name = 'Noname'
    lastname = 'Nolastname'
    age = 0
    course = 1
    
    def __init__(self, name, lastname, age, course):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.course = course
    
    def __str__(self):
        return f'{self.name} {self.lastname}, {self.age} лет, курс: {self.course}'
        