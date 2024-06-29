"""rename address

Revision ID: 957b04928055
Revises: 1aabad896b13
Create Date: 2024-06-30 00:45:28.918393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '957b04928055'
down_revision = '1aabad896b13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###