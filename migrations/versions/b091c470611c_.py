"""empty message

Revision ID: b091c470611c
Revises: 7050a008008c
Create Date: 2023-12-07 19:15:29.950777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b091c470611c'
down_revision = '7050a008008c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('category', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'category')
    # ### end Alembic commands ###
