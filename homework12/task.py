# Using ORM framework of your choice, create models classes created in Homework 6
# (Teachers, Students, Homework and others). - Target database should be sqlite
# (filename main.db localted in current directory) - ORM framework should support migrations.
#
# Utilizing that framework capabilities, create
#
#  a migration file, creating all necessary database structures.
#  a migration file (separate) creating at least one record in each created database table
#
#  (*) optional task: write standalone script (get_report.py) that
#  retrieves and stores the following information into CSV file report.csv
#
#             for all done (completed) homeworks:
#                 Student name (who completed homework) Creation date Teacher name who created homework
#
# Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.
import datetime
from collections import defaultdict
from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

convention = {
    "all_column_names": lambda constraint, table: "_".join(
        [column.name for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": ("fk__%(table_name)s__%(all_column_names)s__" "%(referred_table_name)s"),
    "pk": "pk__%(table_name)s",
}

# Registry for all tables
metadata = MetaData(naming_convention=convention)
Base = declarative_base()


class Homework(Base):
    __tablename__ = "homework"
    homework_id = Column(Integer, primary_key=True)
    task_text = Column(String)
    created = datetime.datetime.now()
    deadline = Column(Integer)


class HomeworkResult(Base):
    __tablename__ = "homework_result"
    result_id = Column(Integer, primary_key=True)
    solution = Column(String)
    homework = Column(Integer, ForeignKey("homework.homework_id"))
    author = Column(Integer, ForeignKey("student.student_id"))


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


class Teacher(Base):
    __tablename__ = "teacher"
    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
