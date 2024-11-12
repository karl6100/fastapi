"""add content to posts table

Revision ID: 18769e58d0c4
Revises: c30055a34f74
Create Date: 2024-11-12 11:31:15.241262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18769e58d0c4'
down_revision: Union[str, None] = 'c30055a34f74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')

    pass
