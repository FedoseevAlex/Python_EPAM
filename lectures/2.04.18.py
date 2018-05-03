# Написать класс для вина #L5.1
"""
class Wine:
    def __init__(self, name, year, location):
        self.name = name
        self.year = year
        self.loc = location

    def set_name(self, name):
        if type(name) == str:
            self.name  = name
        else:
            print('wrong name')


    def set_year(self, year):
        if type(year) == int:
            self.year = 1921
        else:
            print('wrong year')


    def age(self, now):
        if type(now) == int:
            return now  - self.year
        else:
            print('wrong year')

    def set_location(self, location):
        if type(location) == str:
            self.loc =  location
        else:
            print('wrong location')

f = Wine("Cheteau", 1912, "France")
print(f.age(2021))
"""

# Написать класс, который представляет любого человека в школе
# #L5.2
"""
class SchoolMember:
    def __init__(self, name, age):
        if type(age) == int:
            self.age = age
        if type(name) == str:
            self.name = name
            print('Создан SchoolMember: {}'.format(self.name))

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

class Teacher(SchoolMember):
    def __init__(self, salary):
        if type(salary) == int:
            self.salary = salary
            super().__init__(initial)
            print('Создан Teacher: {}'.format(self.name))

    def get_salary(self):
        return self.salary


class Student(SchoolMember):
    def __init__(self, grades):
        if type(grades) == int:
            self.grades = grades
            print('Создан Student: {}'.format(self.name))

    def get_grades(self):
        return self.grades
"""
