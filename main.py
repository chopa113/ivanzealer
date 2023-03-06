import socket
from requests import get
import requests


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text

print(f'host: {hostname}')
print(f'lip: {local_ip}')
print(f'pip: {public_ip}')


token = "5701589055:AAHL1gbfBrCO6PFf-wGoOJe9QdQRmUNIC-0"
chat_id = "1104502854"
text = (f"local ip = {local_ip} ,public ip = {public_ip} ,hostname = {hostname} ")
url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
results = requests.get(url_req)
print(results.json())
