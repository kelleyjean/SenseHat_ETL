from sqlalchemy import *
from sqlalchemy.engine.url import URL
from Database import settings
from Database.settings import DATABASE


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    database = create_engine(URL(**settings.DATABASE))
    return database

