import os

from ollama import Client


def respond(messages, model):
    client = Client(
        host=os.environ.get("OLLAMA_HOST"),
        headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_AUTH")},
    )
    llm_messages = []
    for i, message in enumerate(messages):
        llm_messages.append({"role": "user" if i % 2 == 0 else "agent", "content": message})
    response = client.chat(model=model, messages=llm_messages)
    print(llm_messages)
    return response["message"]["content"].strip()
