from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
# from .Base import Base

class Base(DeclarativeBase):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer(),primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())
    lastname: Mapped[str] = mapped_column(String())
    icon: Mapped[Optional[str]] = mapped_column(String())
    teams:Mapped[Optional[list["Users_Teams"]]] = relationship("Users_Teams", back_populates='users')


class Teams(Base):
    __tablename__ = "Teams"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())

    users: Mapped[Optional[list["Users_Teams"]]] = relationship("Users_Teams", back_populates='teams')

class Users_Teams(Base):
    __tablename__ = "Users_Teams"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    users_id: Mapped[int] = mapped_column(ForeignKey(Users.id))
    teams_id: Mapped[int] = mapped_column(ForeignKey(Teams.id))
    role: Mapped[str] = mapped_column(String())

    users = relationship('Users', back_populates="teams")
    teams = relationship('Teams', back_populates='users')
