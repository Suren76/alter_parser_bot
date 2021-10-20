from PIL import Image
from pathlib import Path
import pytesseract
import json
from googletrans import Translator
from pyrogram import Client
import os

f = open("kik_telegram_result.json", "r")
f = str(f)
print(len(f), type(f))

j = json.loads(open("kik_telegram_result.json", "r"))

