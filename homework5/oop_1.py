"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    def __init__(self, task_text: str, days: int):
        self.text = task_text
        if days < 0:
            raise ValueError("can't be negative")
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.created + self.deadline < datetime.datetime.now()


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(task_text: str, days: int) -> Homework:
        return Homework(task_text, days)


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, hw: Homework) -> Homework:
        if hw.is_active():
            return hw
        else:
            print('You are late')


if __name__ == '__main__':
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")

    expired_homework = teacher.create_homework("Learn functions", 0)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
