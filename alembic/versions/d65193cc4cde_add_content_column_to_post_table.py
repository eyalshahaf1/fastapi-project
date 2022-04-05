"""add content column to post table

Revision ID: d65193cc4cde
Revises: 9f65bbf1502b
Create Date: 2022-04-05 13:22:02.373008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65193cc4cde'
down_revision = '9f65bbf1502b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
