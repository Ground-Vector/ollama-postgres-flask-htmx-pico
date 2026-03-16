from library import database_table, database_query


def get_users(db):
    return [row["prompt"] for row in database_table(db, "select prompt from prompts order by id")]


def add_user(db, name):
    return database_query(db, "insert into prompts (prompt) values (%s)", (name,))
