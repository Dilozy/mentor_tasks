from datetime import datetime, date

from sqlalchemy import extract, func, or_, select
from sqlalchemy.orm import joinedload, selectinload

from db.database import session_factory
from models import Author, Book, Review


class SQLAlchemyQueries:
    def __init__(self):
        self._session = None

    def __enter__(self):
        self._session = session_factory()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._session.rollback()
        else:
            self._session.commit()
        self._session.close()

    def find_first_name_john(self):
        query = select(Author).filter(Author.first_name == "John")
        return self._session.execute(query).scalars().all()

    def find_not_doe_last_name(self):
        query = select(Author).filter(Author.last_name != "Doe")
        return self._session.execute(query).scalars().all()

    def less_than_500_book_price(self):
        query = select(Book).filter(Book.price < 500)
        return self._session.execute(query).scalars().all()

    def book_price_lte_300(self):
        query = select(Book).filter(Book.price <= 300)
        return self._session.execute(query).scalars().all()
    
    def book_price_gt_1000(self):
        query = select(Book).filter(Book.price > 1000)
        return self._session.execute(query).scalars().all()

    def book_price_gte_750(self):
        query = select(Book).filter(Book.price >= 750)
        return self._session.execute(query).scalars().all()
    
    def book_with_django_in_name(self):
        query = select(Book).filter(Book.title.like("%Django%"))
        return self._session.execute(query).scalars().all()
    
    def book_with_python_in_name(self):
        query = select(Book).filter(Book.title.icontains("python"))
        return self._session.execute(query).scalars().all()
    
    def book_title_startswith_advanced(self):
        query = select(Book).filter(Book.title.startswith("Advanced"))
        return self._session.execute(query).scalars().all()
    
    def book_title_startswith_pro(self):
        query = select(Book).filter(Book.title.istartswith("pro"))
        return self._session.execute(query).scalars().all()
    
    def book_title_endswith_guide(self):
        query = select(Book).filter(Book.title.endswith("Guide"))
        return self._session.execute(query).scalars().all()
    
    def book_title_endswith_tutorial(self):
        query = select(Book).filter(Book.title.iendswith("tutorial"))
        return self._session.execute(query).scalars().all()
    
    def find_all_reviews_without_a_comment(self):
        query = select(Review).filter(Review.comment.is_(None))
        return self._session.execute(query).scalars().all()
    
    def find_all_reviews_with_a_comment(self):
        query = select(Review).filter(Review.comment.isnot(None))
        return self._session.execute(query).scalars().all()
    
    def find_authors_with_specified_ids(self):
        query = select(Author).filter(Author.id.in_([1, 3, 5]))
        return self._session.execute(query).scalars().all()
    
    def find_books_published_in_2023(self):
        query = select(Book).filter(
            Book.published_date.between(datetime(2023, 1, 1), datetime(2023, 12, 31))
            )
        return self._session.execute(query).scalars().all()
    
    def find_books_name_startswith_python(self):
        query = select(Book).filter(Book.title.like("Python %"))
        return self._session.execute(query).scalars().all()
    
    def find_authors_last_name_contains_mc(self):
        query = select(Author).filter(Author.last_name.ilike("%mc%"))
        return self._session.execute(query).scalars().all()
    
    def find_2024_books(self):
        query = select(Book).filter(extract("YEAR", Book.published_date) == 2024)
        return self._session.execute(query).scalars().all()
    
    def find_books_published_in_june(self):
        query = select(Book).filter(extract("MONTH", Book.published_date) == 6)
        return self._session.execute(query).scalars().all()

    def find_reviews_written_at_11th_day(self):
        query = select(Review).filter(extract("DAY", Review.created_at) == 11)
        return self._session.execute(query).scalars().all()
    
    def books_published_at_week_23(self):
        query = select(Book).filter(extract("WEEK", Book.published_date) == 23)
        return self._session.execute(query).scalars().all()
    
    def reviews_created_at_tuesday(self):
        query = select(Review).filter(extract("DOW", Review.created_at) == 2)
        return self._session.execute(query).scalars().all()
    
    def book_published_at_second_quarter_of_a_year(self):
        query = select(Book).filter(extract("MONTH", Book.published_date).in_([4, 5, 6]))
        return self._session.execute(query).scalars().all()
    
    def reviews_created_at(self, date: date):
        query = select(Review).filter(
            extract("YEAR", Review.created_at) == date.year,
            extract("MONTH", Review.created_at) == date.month,
            extract("DAY", Review.created_at) == date.day
            )
        return self._session.execute(query).scalars().all()
    
    def reviews_created_at_15_30(self):
        query = select(Review).filter(
            extract("HOUR", Review.created_at) == 15,
            extract("MINUTE", Review.created_at) == 30,
            func.floor(extract("SECOND", Review.created_at)) == 0
            )
        return self._session.execute(query).scalars().all()
    
    def reviews_created_at_15(self):
        query = select(Review).filter(extract("HOUR", Review.created_at) == 15)
        return self._session.execute(query).scalars().all()
    
    def reviews_created_at_30_mins(self):
        query = select(Review).filter(extract("MINUTE", Review.created_at) == 30)
        return self._session.execute(query).scalars().all()
    
    def review_created_at_0_seconds(self):
        query = select(Review).filter(
            func.floor(extract("SECOND", Review.created_at)) == 0
        )
        return self._session.execute(query).scalars().all()

    def books_from_author_with_author_example_com_email(self):
        query = select(Book).join(Author, Author.id == Book.author_id) \
                            .filter(Author.email == "author@example.com").all()
        return self._session.execute(query).scalars().all()
    
    def books_from_authors_with_smith_in_last_name(self):
        query = select(Book).join(Author) \
                            .filter(Author.last_name.ilike("%smith%"))
        return self._session.execute(query).scalars().all()
    
    def authors_with_more_than_five_books(self):
        query = select(Author).join(Author.books) \
                            .group_by(Author.id).having(func.count(Book.id) > 5)
        return self._session.execute(query).scalars().all()
    
    def books_with_genre_fiction(self):
        query = select(Book).filter(Book.meta["genre"].as_string() == "fiction")
        return self._session.execute(query).scalars().all()    
    
    def books_with_tag_bestseller(self):
        query = select(Book).filter(Book.meta["tags"] \
                                        .as_string().icontains("bestseller"))
        return self._session.execute(query).scalars().all()
    
    def books_with_price_same_as_discount(self):
        query = select(Book).filter(Book.price == Book.discount)
        return self._session.execute(query).scalars().all()
    
    def books_with_price_higher_than_discount(self):
        query = select(Book).filter(Book.price > Book.discount)
        return self._session.execute(query).scalars().all()
    
    def authors_with_name_alice_and_last_name_not_brown(self):
        query = select(Author).filter(or_(
            Author.first_name == "Alice",
            Author.last_name != "Brown"
        ))
        return self._session.execute(query).scalars().all()

    def count_authors_books(self):
        query = select(Author, func.count(Book.id).label("books_count")) \
                            .join(Author.books).group_by(Author.id)
        return self._session.execute(query).all()
    
    def books_avg_rating(self):
        query = select(Book, func.round(func.avg(Review.rating).label("avg_rating"), 1)) \
                            .join(Book.reviews).group_by(Book.id)
        return self._session.execute(query).all()
    
    def book_final_price(self):
        query = select(Book, (Book.price - Book.discount).label("final_price"))
        return self._session.execute(query).all()
    
    def books_and_authors_in_one_query(self):
        query = select(Book).options(joinedload(Book.author))
        return self._session.execute(query).scalars().all()
    
    def books_and_authors_in_two_queries(self):
        query = select(Book).options(selectinload(Book.author))
        return self._session.execute(query).scalars().all()

def main():
    with SQLAlchemyQueries() as queries:
        res = queries.book_final_price()
        print(res)

if __name__ == "__main__":
    main()
