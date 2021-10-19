import json
from googletrans import Translator
from pyrogram import Client
import os
import pytesseract
from PIL import Image

if "downloads" in os.listdir():
    # os.rmdir("downloads")
    os.system("rm -rf downloads")

api_id = 8553553
api_hash = "e41a7ae054a851e4e94b96dc31ffb28e"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "kik test ")
    get_messages = app.get_history("kikobzor", limit=60)

messages = json.loads(str(get_messages))
# print(len(messages), type(messages))


def make_past_json(messages):
    posts = {}

    for message in messages:
        post_body = {}
        # print(post_body)

        message_id = message["message_id"]
        post_body["message_id"] = message_id
        # print("message_id", message_id, type(message_id))

        date = message["date"][:-3]
        # post_body["date"] = date
        # print("date", date, type(date))

        #    "message_id", "photo", "text", "caption", "date"
        # print("message", type(message))

        if "photo" in message:
            photo = message["photo"]['file_id']
            post_body["photo"] = f"{photo}.png"
            # print("photo", photo, type(photo))

        # if "video" in message:
        #     photo = message["video"]['file_id']
        #     post_body["photo"] = f"{photo}.mp4"
        #     # print("photo", photo, type(photo))

        if "text" in message:
            text = message["text"]
            post_body["text"] = Translator().translate(text).text

        if "caption" in message:
            caption = message["caption"]
            post_body["caption"] = Translator().translate(caption).text

        if date in posts.keys():
            posts[date].update(post_body)
        else:
            posts[date] = post_body
    return posts


# json_file = open("kik_telegram_.json", "w+")
# json_file.write(str(make_past_json(messages)))
# json_file.close()

#    Download photos
posts = make_past_json(messages)
with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "kik test ")
    p = 2
    for post in posts.values():
        # print(post)
        if "photo" not in post.keys():
            print(post)
            continue
            # media_id = post['video']
            # print(media_id)
            # app.download_media(media_id[:-4], media_id)
            # continue
        if "photo" in post.keys() and len(post.keys()) == 2:
            file = app.download_media(post['photo'][:-4])
            image = Image.open(file)

            # im.show()
            width, height = image.size
            print(width, type(height))

            a = (0, 0, width, height / 2)
            b = (0, height / 2, width, height)

            print(1)
            img_crop_1 = image.crop(a).save("downloads/"+post['photo'])  # image
            print(2)
            img_crop_2 = image.crop(b)  # future text
            print(3)

            text = Translator().translate(pytesseract.image_to_string(image=img_crop_2, lang="rus+eng")).text
            print("translated")
            post["text_b"] = text

            if p != 0:
                print(post)
                p -= 1

            continue

        media_id = post['photo']
        print(media_id)
        app.download_media(media_id[:-4], media_id)
    print(len(posts))


json_file = open("kik_telegram_result.json", "w+")
json_file.write(str(posts))
json_file.close()
