create table chats (
    id serial primary key,
    message text,
    model text
);

create table messages (
    id serial primary key,
    chat_id int references chats(id),
    message text
);

create index messages_chat_id on messages(chat_id);
