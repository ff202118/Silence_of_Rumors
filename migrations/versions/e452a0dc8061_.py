"""empty message

Revision ID: e452a0dc8061
Revises: 30085d2b33b4
Create Date: 2023-12-14 14:01:08.428820

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e452a0dc8061'
down_revision = '30085d2b33b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('comments_count', sa.Integer(), nullable=True))
    op.add_column('news', sa.Column('participants', sa.Integer(), nullable=True))
    op.add_column('news', sa.Column('picture', sa.String(length=128), nullable=True))
    op.add_column('news', sa.Column('comment1', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment2', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment3', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment4', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment5', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment6', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment7', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment8', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment9', sa.String(length=128), nullable=False))
    op.add_column('news', sa.Column('comment10', sa.String(length=128), nullable=False))
    op.drop_column('news', 'hot')
    op.drop_column('news', 'image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('image_link', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('news', sa.Column('hot', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('news', 'comment10')
    op.drop_column('news', 'comment9')
    op.drop_column('news', 'comment8')
    op.drop_column('news', 'comment7')
    op.drop_column('news', 'comment6')
    op.drop_column('news', 'comment5')
    op.drop_column('news', 'comment4')
    op.drop_column('news', 'comment3')
    op.drop_column('news', 'comment2')
    op.drop_column('news', 'comment1')
    op.drop_column('news', 'picture')
    op.drop_column('news', 'participants')
    op.drop_column('news', 'comments_count')
    # ### end Alembic commands ###