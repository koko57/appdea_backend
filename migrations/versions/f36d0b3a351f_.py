"""empty message

Revision ID: f36d0b3a351f
Revises: 
Create Date: 2020-08-07 16:45:42.791413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f36d0b3a351f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appdea', sa.Column('name2', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appdea', 'name2')
    # ### end Alembic commands ###
