from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'f95d1a8bdba0'
down_revision: Union[str, Sequence[str], None] = 'af7519bf2c9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('task', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_foreign_key(None, 'task', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('user', sa.Column('password', sa.String(length=256), nullable=False))
    op.drop_column('user', 'hashed_password')


def downgrade() -> None:
    op.add_column('user', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('user', 'password')
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.alter_column('task', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
