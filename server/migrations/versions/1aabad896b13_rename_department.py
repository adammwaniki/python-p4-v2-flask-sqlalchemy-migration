"""rename department

Revision ID: 1aabad896b13
Revises: aec8ae92c4f4
Create Date: 2024-06-30 00:37:30.298228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aabad896b13'
down_revision = 'aec8ae92c4f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
