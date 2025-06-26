"""empty message

Revision ID: dc897cdcbc58
Revises: 92e48f94a310
Create Date: 2025-06-25 13:43:55.561266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from db.init_data import init_data

# revision identifiers, used by Alembic.
revision: str = 'dc897cdcbc58'
down_revision: Union[str, Sequence[str], None] = '92e48f94a310'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    init_data()


def downgrade() -> None:
    """Downgrade schema."""
    pass
