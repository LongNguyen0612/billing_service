"""Modify month field on subscription

Revision ID: ee23484f483a
Revises: 76c445bbdf3d
Create Date: 2022-07-01 22:57:13.342733

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee23484f483a'
down_revision = '76c445bbdf3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('month', sa.Integer(), nullable=True))
    op.drop_column('subscriptions', 'quantity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('quantity', postgresql.DOUBLE_PRECISION(precision=53), server_default=sa.text("'0'::double precision"), autoincrement=False, nullable=True))
    op.drop_column('subscriptions', 'month')
    # ### end Alembic commands ###
