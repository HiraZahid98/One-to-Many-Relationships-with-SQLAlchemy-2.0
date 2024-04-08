# in this file we are defining database model for tables using sql alchemy

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
"""
    table program
        - id int pk
        - name str
        - years_of_study

    table courses
        - id int pk
        - title
        - code
        - program_id => fk => program.id
"""

class Base(DeclarativeBase):
    pass

class Program(Base):
    __tablename__ = "programs"
    id : Mapped[int] = mapped_column(primary_key = True)
    name : Mapped[str] = mapped_column(nullable = False)
    years_of_study : Mapped[int] = mapped_column(nullable = False)
    courses : Mapped[List['Course']] = relationship(backref='program')
    def __repr__(self) -> str:
        return f"Program name {self.name}"

class Course(Base):
    __tablename__ = "courses"
    id : Mapped[int] = mapped_column(primary_key = True)
    title : Mapped[str] = mapped_column(nullable = False)
    code : Mapped[str] = mapped_column(nullable = False)
    program_id : Mapped[int] = mapped_column(ForeignKey("programs.id", ondelete='CASCADE'))

    def __repr__(self) -> str:
        return f"Course name {self.title}"