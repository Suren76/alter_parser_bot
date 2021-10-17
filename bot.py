from pyrogram import Client

api_id = 8553553
api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"


with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "kik test ")
    got_messages = app.get_history("kikobzor",limit=5)
    print(got_messages)