"""empty message

Revision ID: 6e13529960fc
Revises: 6c9e10dfed40
Create Date: 2020-10-10 16:27:12.011952

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6e13529960fc'
down_revision = '6c9e10dfed40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('accuracy', sa.Integer(), nullable=True),
    sa.Column('mistakes', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tests',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    op.drop_table('results')
    # ### end Alembic commands ###
