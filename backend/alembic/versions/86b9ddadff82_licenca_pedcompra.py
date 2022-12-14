"""licenca-pedcompra

Revision ID: 86b9ddadff82
Revises: 252ea9d098a3
Create Date: 2022-11-26 08:46:44.429648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b9ddadff82'
down_revision = '252ea9d098a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('licencas', sa.Column('pedcompra', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('licencas', 'pedcompra')
    # ### end Alembic commands ###
