import enum
from typing import List

from sqlalchemy import Integer, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.models.base import Base


class UserGroupEnum(str, enum.Enum):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"


class GenderEnum(str, enum.Enum):
    MAN = "man"
    WOMAN = "woman"


class UserGroupModel(Base):
    __tablename__ = "user_groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[UserGroupEnum] = mapped_column(
        Enum(UserGroupEnum), unique=True, nullable=False
    )

    users: Mapped[List["UserModel"]] = relationship("UserModel", back_populates="group")

    def __repr__(self) -> str:
        return f"<UserGroupModel(id={self.id}, name={self.name})>"
