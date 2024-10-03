"""Initial migration

Revision ID: 5627190f8718
Revises: 
Create Date: 2024-10-03 10:27:29.257875

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5627190f8718"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "breeds",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("breeds", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_breeds_id"), ["id"], unique=False)
        batch_op.create_index(batch_op.f("ix_breeds_name"), ["name"], unique=True)

    op.create_table(
        "kittens",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("color", sa.String(), nullable=True),
        sa.Column("age_in_months", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("breed_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["breed_id"],
            ["breeds.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("kittens", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_kittens_id"), ["id"], unique=False)
        batch_op.create_index(batch_op.f("ix_kittens_name"), ["name"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("kittens", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_kittens_name"))
        batch_op.drop_index(batch_op.f("ix_kittens_id"))

    op.drop_table("kittens")
    with op.batch_alter_table("breeds", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_breeds_name"))
        batch_op.drop_index(batch_op.f("ix_breeds_id"))

    op.drop_table("breeds")
    # ### end Alembic commands ###
