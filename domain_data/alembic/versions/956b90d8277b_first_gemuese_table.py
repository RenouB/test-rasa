"""first gemuese table

Revision ID: 956b90d8277b
Revises: bc25b5f8939f
Create Date: 2021-12-08 14:19:47.124084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956b90d8277b'
down_revision = 'bc25b5f8939f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'gemuese',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('veg_type', sa.String(), nullable=False),
        sa.Column('variety', sa.String()),
        sa.Column('length', sa.Integer()),
        sa.Column('price', sa.Integer())
    )


def downgrade():
    op.drop_table('gemuese')
