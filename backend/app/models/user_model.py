from sqlalchemy import column, Integer, String ,Float


class User():
    __tablename__ = "user"

    id: Mapped[int] = mapped_colum(primary_key=True)
    name: Mapped[str] = mapped_colum(String(20))
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    location: Mapped[str] = mapped_column(String(20))
