revision = "169ad57156f0"
down_revision = "29b4c2bfce6d"

import sqlalchemy as sa
from alembic import op
from homework12 import task
from sqlalchemy import orm


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    session.add_all(
        [
            task.Teacher(first_name="dub", last_name="bub"),
            task.Student(first_name="lupa", last_name="pupa"),
            task.HomeworkResult(solution="something", homework=1, author=1),
            task.Homework(task_text="task1", deadline=5),
        ]
    )

    session.commit()


def downgrade():

    bind = op.get_bind()
    session = orm.Session(bind=bind)
    session.query(task.Teacher).filter(task.Teacher.teacher_id == 1).delete()
    session.query(task.Student).filter(task.Student.student_id == 1).delete()
    session.query(task.HomeworkResult).filter(
        task.HomeworkResult.result_id == 1
    ).delete()
    session.query(task.Homework).filter(task.Homework.homework_id == 1).delete()
    session.commit()
