"""add for entity field to playlists

Revision ID: 7417c8eb70d8
Revises: cf3d365de164
Create Date: 2020-03-15 17:49:32.365732

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '7417c8eb70d8'
down_revision = '8739ae9fa28b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playlist', sa.Column('for_entity', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_playlist_for_entity'), 'playlist', ['for_entity'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_playlist_for_entity'), table_name='playlist')
    op.drop_column('playlist', 'for_entity')
    # ### end Alembic commands ###
