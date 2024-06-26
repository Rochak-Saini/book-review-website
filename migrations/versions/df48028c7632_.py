"""empty message

Revision ID: df48028c7632
Revises: 380b06634f63
Create Date: 2024-04-22 19:56:24.370067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df48028c7632'
down_revision = '380b06634f63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
