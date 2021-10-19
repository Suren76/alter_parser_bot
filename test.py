from PIL import Image
from pathlib import Path
import pytesseract
import json
from googletrans import Translator
from pyrogram import Client
import os

api_id = 8553553
api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"
file = Path("downloads/AgACAgIAAx0CQ_FAUQACA0hhbjKGHlumZu1MSQYxa2rYMa1zJwACCbYxG8jdOEuIt4W0zStqv5aE9qkuAAMBAAMCAAN3AAPQgAUAAR4E.png")
im = Image.open(file)

with Client("my_account", api_id, api_hash) as app:
    post_body = {}
    app.send_message("me", "kik test ")
    message = json.loads(str(app.get_history("kikobzor", limit=1)))[0]
    print(message)


    if "photo" in message:
        photo = message["photo"]['file_id']
        post_body["photo"] = f"{photo}.png"
        print("photo", photo, type(photo))

    f = app.download_media(post_body["photo"][:-4], post_body["photo"])

    # f = Path(post_body["photo"])
    im = Image.open(f)

    # im.show()
    width, height = im.size
    print(width, type(height))
    top = 0
    left = 0
    right = 0
    bottom = 0
    a = (0, 0, width, height / 2)
    b = (0, height / 2, width, height)

    print(1)
    img_crop_1 = im.crop(a).save("1.jpg")
    print(2)
    img_crop_2 = im.crop(b)
    print(3)

#     # pytesseract.pytesseract.tesseract_cmd("tesseract")
    #print(pytesseract.get_languages())
    text = Translator().translate(pytesseract.image_to_string(image=img_crop_2, lang="rus+eng")).text
    print(text)

