"""add foreign-key to post table

Revision ID: 769155febe44
Revises: b20475fb0fd9
Create Date: 2024-11-12 11:48:45.341141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '769155febe44'
down_revision: Union[str, None] = 'b20475fb0fd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fkey', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fkey', 'posts')
    op.drop_column('posts','owner_id')
    pass
