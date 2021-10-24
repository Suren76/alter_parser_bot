import json
import requests
import PIL

PIL.

RequestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=english'

LicenseCode = "45E89313-84F2-4FE7-BFA3-7EEEEEFF46F1"
UserName =  "SUREN"

FilePath = "/storage/emulated/0/Pictures/Telegram/20211019_225302.jpg"

#j = requests.get("http://www.ocrwebservice.com/restservices/getAccountInformation")

with open(FilePath, 'rb') as image_file:
    image_data = image_file.read()
print(image_file)
r = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))
print(r)
#print(j)
# jobj = json.loads(r.content)

print(r.status_code)
