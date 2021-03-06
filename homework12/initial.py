"""initial

Revision ID: c8e0addb226d
Revises: 
Create Date: 2021-04-30 14:09:19.127938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e0addb226d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('teacher_id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_table('homework_results',
    sa.Column('result_id', sa.INTEGER(), nullable=False),
    sa.Column('solution', sa.VARCHAR(), nullable=True),
    sa.Column('homework', sa.INTEGER(), nullable=True),
    sa.Column('author', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['homework'], ['homeworks.homework_id'], ),
    sa.PrimaryKeyConstraint('result_id')
    )
    op.create_table('homeworks',
    sa.Column('homework_id', sa.INTEGER(), nullable=False),
    sa.Column('task_text', sa.VARCHAR(), nullable=True),
    sa.Column('created_date', sa.DATETIME(), nullable=True),
    sa.Column('deadline', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('homework_id')
    )
    op.create_table('students',
    sa.Column('student_id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('homeworks')
    op.drop_table('homework_results')
    op.drop_table('teachers')
    # ### end Alembic commands ###
