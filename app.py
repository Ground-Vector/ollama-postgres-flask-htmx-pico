import os

from flask import Flask, render_template, request, redirect, url_for
from ollama import Client

from database import get_chats, add_chat, get_chat, get_messages, add_message
from library import database_handle
from llm import respond

app = Flask(__name__)
db = database_handle()
models = os.environ.get("OLLAMA_MODELS").split(",")


@app.route("/", methods=["GET", "POST"])
def chats():
    if request.method == "POST":
        message = request.form.get("message")
        model = request.form.get("model")
        chat_id = add_chat(db, message, model)
        return redirect(url_for("chat", chat_id=chat_id))
    return render_template("chats.html", chats=get_chats(db), models=models)


def get_chat_with_messages(db, chat_id):
    chat = get_chat(db, chat_id)
    messages = get_messages(db, chat_id)
    llm_messages = [chat["message"]]
    for message in messages:
        llm_messages.append(message["message"])
    return llm_messages, chat["model"], len(llm_messages) % 2 == 0


@app.route("/chats/<int:chat_id>", methods=["GET", "POST"])
def chat(chat_id):
    if request.method == "POST":
        add_message(db, chat_id, request.form.get("message"))
    return render_template("chat.html", chat_id=chat_id)


@app.route("/chats/<int:chat_id>/messages")
def messages(chat_id):
    messages, model, done = get_chat_with_messages(db, chat_id)
    return render_template("messages.html", messages=messages, done=done)


@app.route("/chats/<int:chat_id>/process")
def process(chat_id):
    messages, model, done = get_chat_with_messages(db, chat_id)
    if not done:
        add_message(db, chat_id, respond(messages, model))
    return ""
