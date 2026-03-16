from library import database_table, database_query


def get_users(db):
    return [row["name"] for row in database_table(db, "select name from users order by id")]


def add_user(db, name):
    return database_query(db, "insert into users (name) values (%s)", (name,))
