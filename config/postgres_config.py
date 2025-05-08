import os

postgres_host = os.getenv('POSTGRES_HOST')
postgres_database = os.getenv('POSTGRES_DB')
postgres_username = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')

if postgres_host is None:
    raise ValueError('You should specify POSTGRES_HOST environment variable to be able to connect to PostgreSQL DB Server.')

if postgres_database is None:
    raise ValueError('You should specify POSTGRES_DB environment variable to be able to connect to PostgreSQL DB Server.')

if postgres_username is None:
    raise ValueError('You should specify POSTGRES_USER environment variable to be able to connect to PostgreSQL DB Server.')

if postgres_password is None:
    raise ValueError('You should specify POSTGRES_PASSWORD environment variable to be able to connect to PostgreSQL DB Server.')
