from library import database_table, database_query


def get_prompts(db):
    return database_table(db, "select prompt, response from prompts order by id")

def get_prompts_without_response(db):
    return database_table(db, "select id, prompt from prompts where response is null order by id")

def add_user(db, name):
    return database_query(db, "insert into prompts (prompt) values (%s)", (name,))

def add_response(db, id, response):
    return database_query(db, "update prompts set response=%s where id=%s", (response, id,))
