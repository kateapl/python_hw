import datetime

import homework6.oop_2 as hw1
import pytest


def test_teacher_created():
    teacher = hw1.Teacher("Daniil", "Shadrin")
    assert (teacher.last_name, teacher.first_name) == ("Shadrin", "Daniil")


def test_student_created():
    student = hw1.Student("Martin", "Septim")
    assert (student.last_name, student.first_name) == ("Septim", "Martin")


def test_homework_created_without_teacher_object():
    hw = hw1.Teacher.create_homework("do something", 10)
    assert (hw.deadline, hw.text) == (datetime.timedelta(days=10), "do something")


def test_homework_late():
    hw = hw1.Teacher.create_homework("late", 0)
    student = hw1.Student("Jon", "Snow")
    with pytest.raises(hw1.DeadlineError):
        student.do_homework(hw, "something")


def test_homework_deadline_is_negative():
    with pytest.raises(ValueError):
        hw = hw1.Teacher.create_homework("late", -1)


def test_create_function_from_object_and_use_it():
    teacher = hw1.Teacher("Daniil", "Shadrin")
    oop_homework = teacher.create_homework("create 2 simple classes", 5)
    assert (oop_homework.deadline, oop_homework.text) == (
        datetime.timedelta(days=5),
        "create 2 simple classes",
    )


def test_attribute_error_in_homework_result():
    student = hw1.Student("Jon", "Snow")
    hw = 1
    solution = "You know nothing"
    with pytest.raises(AttributeError):
        result = hw1.HomeworkResult(hw, solution, student)


def test_homework_done():
    opp_teacher = hw1.Teacher("Daniil", "Shadrin")
    advanced_python_teacher = hw1.Teacher("Aleksandr", "Smetanin")
    good_student = hw1.Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = hw1.Teacher.homework_done
    assert temp_1 == temp_2


def test_homework_done_several_results():
    opp_teacher = hw1.Teacher("Daniil", "Shadrin")

    lazy_student = hw1.Student("Roman", "Petrov")
    good_student = hw1.Student("Lev", "Sokolov")
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_2 = good_student.do_homework(docs_hw, "I have done this hw")
    result_3 = lazy_student.do_homework(docs_hw, "done this")

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    assert hw1.Teacher.homework_done[docs_hw] == {"I have done this hw", "done this"}
