#!/usr/bin/env/ python3.6
# Task #L5.2 SchoolMember


class SchoolMember:
    """
    Class describing every school member.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print('(Создан {}: {})'.format(SchoolMember.__name__, name))
        
    def show(self) -> None:
        """
        Prints school member data
        :return: None
        """
        to_show = self.__dict__
        print('Имя: "{name}" Возраст: "{age}"'.format(**to_show), end=' ')
        
        
class Teacher(SchoolMember):
    """
    Class describing every teacher in school.
    """
    def __init__(self, name: str, age: int,  salary: int):
        super().__init__(name, age)
        self.salary = salary
        print('(Создан {}: {})'.format(Teacher.__name__, name))

    def show(self) -> None:
        """
        Prints teacher data
        :return: None
        """
        to_show = self.__dict__
        super().show()
        print('Зарплата: "{salary}"'.format(**to_show))


class Student(SchoolMember):
    """
    Class describing school students.
    """
    def __init__(self, name: str, age: int,  grades: int):
        super().__init__(name, age)
        self.grades = grades
        print('(Создан {}: {})'.format(Student.__name__, name))
 
    def show(self) -> None:
        """
        Prints student data
        :return: None
        """
        to_show = self.__dict__
        super().show()
        print('Оценки: "{grades}"'.format(**to_show))
        
        
persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]

for person in persons:
    person.show()
