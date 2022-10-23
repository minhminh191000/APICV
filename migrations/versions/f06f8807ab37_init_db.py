"""init db

Revision ID: f06f8807ab37
Revises: 04cb38b59af8
Create Date: 2022-10-02 09:24:52.320290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06f8807ab37'
down_revision = '04cb38b59af8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('frofession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('frofession_name', sa.String(length=255), nullable=False),
    sa.Column('describe', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('frofession_name')
    )
    op.create_table('careers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('careers_name', sa.String(length=255), nullable=False),
    sa.Column('describe', sa.String(length=1000), nullable=True),
    sa.Column('frofession_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['frofession_id'], ['frofession.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('careers_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('careers')
    op.drop_table('frofession')
    # ### end Alembic commands ###
