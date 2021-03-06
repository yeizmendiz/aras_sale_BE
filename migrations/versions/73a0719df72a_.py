"""empty message

Revision ID: 73a0719df72a
Revises: 9d4c28b51e52
Create Date: 2021-02-22 20:05:22.431938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '73a0719df72a'
down_revision = '9d4c28b51e52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('working_id', sa.Integer(), nullable=False))
    op.alter_column('order', 'notes',
               existing_type=mysql.VARCHAR(length=250),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'notes',
               existing_type=mysql.VARCHAR(length=250),
               nullable=False)
    op.drop_column('order', 'working_id')
    # ### end Alembic commands ###
