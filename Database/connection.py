import psycopg2


def connect():
    conn = psycopg2.connect(user='postgres', password='password', database='yourdatabase',
                            host='localhost', port='5432')

