"""add transaction model object

Revision ID: b8757cb49af5
Revises: 81f8742dafcd
Create Date: 2019-07-20 00:35:00.041325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8757cb49af5'
down_revision = '81f8742dafcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=140), nullable=True),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_timestamp'), 'transaction', ['timestamp'], unique=False)
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_transaction_timestamp'), table_name='transaction')
    op.drop_table('transaction')
    # ### end Alembic commands ###
