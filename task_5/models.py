from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric, JSON, Text, text

from db.database import Base


class Author(Base):
    __tablename__ = "author"

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name} {self.last_name})"


class Book(Base):
    __tablename__ = "book"

    title: Mapped[str] = mapped_column(String(200))
    author_id: Mapped["Author"] = mapped_column(ForeignKey("author.id",
                                                           ondelete="CASCADE"))
    author: Mapped["Author"] = relationship(back_populates="books")
    published_date: Mapped[datetime]
    price: Mapped[Decimal] = mapped_column(Numeric(precision=6, scale=2))
    discount: Mapped[Decimal] = mapped_column(Numeric(precision=6, scale=2),
                                              default=0)
    meta: Mapped[dict] = mapped_column(JSON, default=dict)
    reviews: Mapped[list["Review"]] = relationship(back_populates="book")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title})"


class Review(Base):
    __tablename__ = "review"

    book_id: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    book: Mapped["Book"] = relationship(back_populates="reviews")
    rating: Mapped[int]
    comment: Mapped[str] = mapped_column(Text(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
        )