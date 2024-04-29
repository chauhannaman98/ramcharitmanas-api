"""Initial migration

Revision ID: dfd423398585
Revises: 
Create Date: 2024-04-29 16:48:48.725246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfd423398585'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manas_chapter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=True),
    sa.Column('name_transliterated', sa.UnicodeText(), nullable=True),
    sa.Column('name_translated', sa.UnicodeText(), nullable=True),
    sa.Column('chapter_number', sa.Integer(), nullable=True),
    sa.Column('name_meaning', sa.UnicodeText(), nullable=True),
    sa.Column('chapter_summary', sa.UnicodeText(), nullable=True),
    sa.Column('chapter_summary_hindi', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manas_verses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('verse_number', sa.Integer(), nullable=True),
    sa.Column('chapter_number', sa.Integer(), nullable=True),
    sa.Column('verse_type', sa.UnicodeText(), nullable=True),
    sa.Column('verse_text', sa.UnicodeText(), nullable=True),
    sa.Column('transliteration', sa.UnicodeText(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_number'], ['manas_chapter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manas_translations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('verse_id', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=255), nullable=True),
    sa.Column('translation', sa.UnicodeText(), nullable=True),
    sa.ForeignKeyConstraint(['verse_id'], ['manas_verses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manas_translations')
    op.drop_table('manas_verses')
    op.drop_table('manas_chapter')
    # ### end Alembic commands ###
