import os

from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, DeclarativeBase, 
                            Mapped, mapped_column)
from dotenv import load_dotenv


load_dotenv()


def get_db_url():
    url_args = (os.getenv("DB_USER"), os.getenv("DB_PASSWORD"),
            os.getenv("DB_HOST"), os.getenv("DB_PORT"),
            os.getenv("DB_NAME"))
    
    return "postgresql+psycopg://{}:{}@{}:{}/{}".format(*url_args)


engine = create_engine(get_db_url(), echo=True)

session_factory = sessionmaker(
    bind=engine,
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
