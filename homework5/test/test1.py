import datetime

import homework5.oop_1 as hw1
import pytest


def test_teacher_created():
    teacher = hw1.Teacher("Daniil", "Shadrin")
    assert (teacher.last_name, teacher.first_name) == ("Shadrin", "Daniil")


def test_student_created():
    student = hw1.Student("Martin", "Luther")
    assert (student.last_name, student.first_name) == ("Luther", "Martin")


def test_homework_created_without_teacher_object():
    hw = hw1.Teacher.create_homework("do something", 10)
    assert (hw.deadline, hw.text) == (datetime.timedelta(days=10), "do something")


def test_homework_late(capsys):
    hw = hw1.Teacher.create_homework("late", 0)
    student = hw1.Student("Roman", "Petrov")
    student.do_homework(hw)
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
    assert student.do_homework(hw) is None


def test_homework_deadline_is_negative():
    with pytest.raises(ValueError):
        hw = hw1.Teacher.create_homework("late", -1)


def test_create_function_from_method_and_use_it():
    teacher = hw1.Teacher("Daniil", "Shadrin")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert (oop_homework.deadline, oop_homework.text) == (
        datetime.timedelta(days=5),
        "create 2 simple classes",
    )
