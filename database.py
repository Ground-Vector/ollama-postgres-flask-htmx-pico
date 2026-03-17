from library import database_table, database_query, database_scalar, database_row


def get_chats(db):
    return database_table(db, "select id, message from chats order by id")


def add_chat(db, message, model):
    return database_scalar(db, "insert into chats (message, model) values (%s, %s) returning id", (message, model))


def get_chat(db, id):
    return database_row(db, "select message, model from chats where id=%s", (id,))


def get_messages(db, chat_id):
    return database_table(db, "select message from messages where chat_id=%s order by id", (chat_id,))


def add_message(db, chat_id, message):
    return database_query(db, "insert into messages (chat_id, message) values (%s, %s)", (chat_id, message))
