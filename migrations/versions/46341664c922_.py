"""empty message

Revision ID: 46341664c922
Revises: d04a22f76ced
Create Date: 2024-03-23 09:57:34.970109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46341664c922'
down_revision = 'd04a22f76ced'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'news', 'category', ['category_id'], ['id'])
    op.add_column('refute', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'refute', 'category', ['category_id'], ['id'])
    op.add_column('rumors', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rumors', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rumors', type_='foreignkey')
    op.drop_column('rumors', 'category_id')
    op.drop_constraint(None, 'refute', type_='foreignkey')
    op.drop_column('refute', 'category_id')
    op.drop_constraint(None, 'news', type_='foreignkey')
    op.drop_column('news', 'category_id')
    # ### end Alembic commands ###
