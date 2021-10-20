import json

file = open("kik_telegram_result.json", "r").read()

posts = json.loads(file)

for post in posts:
    if "photo" not in posts[post].keys():
        continue
    print(post)
    posts[post]["photo"] = "https://raw.githubusercontent.com/Suren76/alter_parser_bot/main/downloads/"+posts[post]["photo"]

print(posts)

json_file = open("kik_telegram_result_with_urls.json", "w+")
json_file.write(json.dumps(posts))
json_file.close()
