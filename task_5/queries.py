from datetime import datetime, date

from sqlalchemy import extract, func, or_
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
        return self._session.query(Author).filter(Author.first_name == "John").all()

    def find_not_doe_last_name(self):
        return self._session.query(Author).filter(Author.last_name != "Doe").all()

    def less_than_500_book_price(self):
        return self._session.query(Book).filter(Book.price < 500).all()

    def book_price_lte_300(self):
        return self._session.query(Book).filter(Book.price <= 300).all()
    
    def book_price_gt_1000(self):
        return self._session.query(Book).filter(Book.price > 1000).all()

    def book_price_gte_750(self):
        return self._session.query(Book).filter(Book.price >= 750).all()
    
    def book_with_django_in_name(self):
        return self._session.query(Book).filter(Book.title.like("%Django%")).all()
    
    def book_with_python_in_name(self):
        return self._session.query(Book).filter(Book.title.icontains("python")).all()
    
    def book_title_startswith_advanced(self):
        return self._session.query(Book).filter(Book.title.startswith("Advanced")).all()
    
    def book_title_startswith_pro(self):
        return self._session.query(Book).filter(Book.title.istartswith("pro")).all()
    
    def book_title_endswith_guide(self):
        return self._session.query(Book).filter(Book.title.endswith("Guide")).all()
    
    def book_title_endswith_tutorial(self):
        return self._session.query(Book).filter(Book.title.iendswith("tutorial")).all()
    
    def find_all_reviews_without_a_comment(self):
        return self._session.query(Review).filter(Review.comment.is_(None)).all()
    
    def find_all_reviews_with_a_comment(self):
        return self._session.query(Review).filter(Review.comment.isnot(None)).all()
    
    def find_authors_with_special_ids(self):
        return self._session.query(Author).filter(Author.id.in_([1, 3, 5])).all()
    
    def find_books_published_in_2023(self):
        return self._session.query(Book).filter(
            Book.published_date.between(datetime(2023, 1, 1), datetime(2023, 12, 31))
            ).all()
    
    def find_books_name_startswith_python(self):
        return self._session.query(Book).filter(Book.title.like("Python %")).all()
    
    def find_authors_last_name_contains_mc(self):
        return self._session.query(Author).filter(Author.last_name.ilike("%mc%")).all()
    
    def find_2024_books(self):
        return self._session.query(Book).filter(extract("YEAR", Book.published_date) == 2024).all()
    
    def find_books_published_in_june(self):
        return self._session.query(Book.published_date).filter(extract("MONTH", Book.published_date) == 6).all()

    def find_reviews_written_at_11th_day(self):
        return self._session.query(Review).filter(extract("DAY", Review.created_at) == 11).all()
    
    def books_published_at_week_23(self):
        return self._session.query(Book).filter(extract("WEEK", Book.published_date) == 23).all()
    
    def reviews_created_at_tuesday(self):
        return self._session.query(Review.created_at).filter(extract("DOW", Review.created_at) == 2).all()
    
    def book_published_at_second_quarter_of_a_year(self):
        return self._session.query(Book).filter(extract("MONTH", Book.published_date).in_([4, 5, 6])).all()
    
    def reviews_created_at(self, date: date):
        return self._session.query(Review.created_at).filter(
            extract("YEAR", Review.created_at) == date.year,
            extract("MONTH", Review.created_at) == date.month,
            extract("DAY", Review.created_at) == date.day
            ).all()
    
    def reviews_created_at_15_30(self):
        return self._session.query(Review.created_at).filter(
            extract("HOUR", Review.created_at) == 15,
            extract("MINUTE", Review.created_at) == 30,
            func.floor(extract("SECOND", Review.created_at)) == 0
            ).all()
    
    def reviews_created_at_15(self):
        return self._session.query(Review).filter(extract("HOUR", Review.created_at) == 15).all()
    
    def reviews_created_at_30_mins(self):
        return self._session.query(Review).filter(extract("MINUTE", Review.created_at) == 30).all()
    
    def review_created_at_0_seconds(self):
        return self._session.query(Review).filter(
            func.floor(extract("SECOND", Review.created_at)) == 0
        ).all()

    def books_from_author_with_author_example_com_email(self):
        return self._session.query(Book).join(Author, Author.id == Book.author_id) \
                            .filter(Author.email == "author@example.com").all()
    
    def books_from_authors_with_smith_in_last_name(self):
        return self._session.query(Book).join(Author) \
                            .filter(Author.last_name.ilike("%smith%")).all()
    
    def authors_with_more_than_five_books(self):
        return self._session.query(Author).join(Author.books) \
                            .group_by(Author.id).having(func.count(Book.id) > 5).all()
    
    def books_with_genre_fiction(self):
        return self._session.query(Book).filter(Book.meta["genre"].as_string() == "fiction").all()
    
    def books_with_tag_bestseller(self):
        return self._session.query(Book).filter(Book.meta["tags"] \
                                        .as_string().icontains("bestseller")).all()
    
    def books_with_price_same_as_discount(self):
        return self._session.query(Book).filter(Book.price == Book.discount).all()
    
    def books_with_price_higher_than_discount(self):
        return self._session.query(Book).filter(Book.price > Book.discount).all()
    
    def authors_with_name_alice_and_last_name_not_brown(self):
        return self._session.query(Author).filter(or_(
            Author.first_name == "Alice",
            Author.last_name != "Brown"
        )).all()

    def count_authors_books(self):
        return self._session.query(Author, func.count(Book.id).label("books_count")) \
                            .join(Author.books).group_by(Author.id).all()
    
    def books_avg_rating(self):
        return self._session.query(Book, func.round(func.avg(Review.rating).label("avg_rating"), 1)) \
                            .join(Book.reviews).group_by(Book.id).all()
    
    def book_final_price(self):
        return self._session.query(Book, (Book.price - Book.discount).label("final_price")).all()
    
    def books_and_authors_in_one_query(self):
        return self._session.query(Book).options(joinedload(Book.author)).all()
    
    def books_and_authors_in_two_queries(self):
        return self._session.query(Book).options(selectinload(Book.author)).all()

def main():
    with SQLAlchemyQueries() as queries:
        res = queries.books_and_authors_in_two_queries()

if __name__ == "__main__":
    main()