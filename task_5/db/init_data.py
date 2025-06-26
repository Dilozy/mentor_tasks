from datetime import datetime, timedelta
import random

from db.database import session_factory
from models import Book, Author, Review


def init_data():
    # Create test authors
    authors_data = [
        {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'},
        {'first_name': 'John', 'last_name': 'Smith', 'email': 'john.smith@example.com'},
        {'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice.johnson@example.com'},
        {'first_name': 'Bob', 'last_name': 'McDonald', 'email': 'bob.mcdonald@example.com'},
        {'first_name': 'Emily', 'last_name': 'Brown', 'email': 'emily.brown@example.com'},
        {'first_name': 'Michael', 'last_name': 'McAllister', 'email': 'michael.mcallister@example.com'},
        {'first_name': 'Sarah', 'last_name': 'Williams', 'email': 'sarah.williams@example.com'},
        {'first_name': 'David', 'last_name': 'Miller', 'email': 'david.miller@example.com'},
        {'first_name': 'John', 'last_name': 'Davis', 'email': 'john.davis@example.com'},
        {'first_name': 'Jennifer', 'last_name': 'Wilson', 'email': 'jennifer.wilson@example.com'},
        {'first_name': 'Author', 'last_name': 'Example', 'email': 'author@example.com'},
    ]

    with session_factory() as session:
        authors = []
        for data in authors_data:
            author = Author(**data)
            authors.append(author)
            session.add(author)

        # Create test books
        book_titles = [
            "Django for Beginners",
            "Python Crash Course",
            "Advanced Python Programming",
            "Pro Django",
            "Python Guide",
            "The Complete Python Tutorial",
            "Python Cookbook",
            "Fluent Python",
            "Advanced Django Techniques",
            "Professional Python",
            "Python Data Science Handbook",
            "Python Testing Guide",
            "Effective Python",
            "Python for Data Analysis",
            "Python Machine Learning Tutorial",
            "Django REST Framework Guide",
            "Python Web Development",
            "Advanced Algorithms in Python",
            "Pro Python Tips",
            "Python Networking Tutorial"
        ]

        books = []
        for i, title in enumerate(book_titles):
            # Vary publication dates from 2022 to 2024
            year = 2022 + (i % 3)
            month = (i % 12) + 1
            day = (i % 28) + 1
            
            # Create some books published in June
            if i % 5 == 0:
                month = 6
            
            # Create some books published on week 23 (June)
            if i % 7 == 0:
                month = 6
                day = 5 + (i % 20)
            
            published_date = datetime(year, month, day)
            
            # Vary prices from 100 to 1500
            price = 100 + (i * 70)
            if price > 1500:
                price = 1500
            
            # Add some discounts
            discount = 0
            if i % 3 == 0:
                discount = price * 0.1
            elif i % 5 == 0:
                discount = price * 0.2
            
            # Some books with price equal to discount
            if i % 7 == 0:
                discount = price
            
            # Create metadata
            genres = ['fiction', 'non-fiction', 'educational', 'technical']
            tags = ['bestseller', 'new release', 'classic', 'popular']
            
            metadata = {
                'genre': random.choice(genres),
                'tags': random.sample(tags, random.randint(1, 3))
            }
            
            # Assign authors - some authors will have multiple books
            author = authors[i % len(authors)]
            
            book = Book(
                title=title,
                author=author,
                published_date=published_date,
                price=price,
                discount=discount,
                meta=metadata
            )
            books.append(book)
            session.add(book)

        # Create test reviews
        review_comments = [
            "Great book!",
            "Very helpful.",
            "Could be better.",
            "Excellent resource.",
            "Not what I expected.",
            "Highly recommended.",
            "A bit outdated.",
            "Perfect for beginners.",
            "Too advanced for me.",
            "Worth every penny.",
            None,  # Some reviews without comments
            None,
            "Good examples.",
            "Clear explanations.",
            None,
            "The best book on this topic.",
            None,
            "Needs more practical examples.",
            "Well structured.",
            None
        ]

        for i, book in enumerate(books):
            # Create 1-5 reviews per book
            for j in range(random.randint(1, 5)):
                # Vary created_at dates
                created_at = datetime.now() - timedelta(days=random.randint(0, 365))
                
                # Create some reviews on Tuesday
                if j % 3 == 0:
                    created_at = created_at.replace(day=random.randint(1, 28), hour=15, minute=30)
                    while created_at.weekday() != 1:  # Tuesday
                        created_at = created_at - timedelta(days=1)
                
                # Create some reviews at specific times
                if j % 5 == 0:
                    created_at = created_at.replace(hour=15, minute=30, second=0)
                elif j % 7 == 0:
                    created_at = created_at.replace(hour=15, minute=0, second=0)
                elif j % 9 == 0:
                    created_at = created_at.replace(minute=30, second=0)
                elif j % 11 == 0:
                    created_at = created_at.replace(second=0)
                
                comment = random.choice(review_comments)
                
                review = Review(
                    book=book,
                    rating=random.randint(1, 5),
                    comment=comment,
                    created_at=created_at
                )
                session.add(review)

        session.commit()