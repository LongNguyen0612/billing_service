"""Adding order_id field to subscription

Revision ID: 6dda384f817b
Revises: ee23484f483a
Create Date: 2022-07-02 17:02:03.040079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dda384f817b'
down_revision = 'ee23484f483a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('order_id', sa.String(length=36), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscriptions', 'order_id')
    # ### end Alembic commands ###