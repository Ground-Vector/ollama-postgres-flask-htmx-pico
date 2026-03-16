import os

import psycopg


def database_handle():
    db = psycopg.Connection.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
        autocommit=True,
        row_factory=psycopg.rows.dict_row,
    )
    return db


def database_query(db, query, params=()):
    return db.execute(query, params)


def database_scalar(db, query, params=()):
    return next(iter(database_row(db, query, params).values()))


def database_row(db, query, params=()):
    return database_query(db, query, params).fetchone()


def database_table(db, query, params=()):
    return database_query(db, query, params).fetchall()
