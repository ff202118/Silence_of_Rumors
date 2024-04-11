"""empty message

Revision ID: d04a22f76ced
Revises: ded63c6dc18b
Create Date: 2024-02-29 14:10:55.606476

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd04a22f76ced'
down_revision = 'ded63c6dc18b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rate', sa.String(length=16), nullable=False),
    sa.Column('authority', sa.String(length=64), nullable=True),
    sa.Column('source', sa.String(length=64), nullable=False),
    sa.Column('source_url', sa.String(length=128), nullable=False),
    sa.Column('date', sa.String(length=32), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('forward_num', sa.Integer(), nullable=False),
    sa.Column('comment_num', sa.Integer(), nullable=False),
    sa.Column('like_num', sa.Integer(), nullable=False),
    sa.Column('detail_url', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rumors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rate', sa.String(length=16), nullable=False),
    sa.Column('authority', sa.String(length=64), nullable=True),
    sa.Column('source', sa.String(length=64), nullable=False),
    sa.Column('source_url', sa.String(length=128), nullable=False),
    sa.Column('date', sa.String(length=32), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('forward_num', sa.Integer(), nullable=False),
    sa.Column('comment_num', sa.Integer(), nullable=False),
    sa.Column('like_num', sa.Integer(), nullable=False),
    sa.Column('detail_url', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rumors')
    op.drop_table('refute')
    # ### end Alembic commands ###
