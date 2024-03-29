"""empty message

Revision ID: d3c52db587b3
Revises: 
Create Date: 2024-01-26 19:17:11.378687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c52db587b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emotion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emotion', sa.Text(), nullable=True),
    sa.Column('project', sa.String(length=255), nullable=True),
    sa.Column('sentiment', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emotion')
    # ### end Alembic commands ###
