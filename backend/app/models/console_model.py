from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import column, Integer, Boolean, String, ForeignKey
from app.core.database import Base

class Console(Base):
    __tablename__ = "console"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="consoles")