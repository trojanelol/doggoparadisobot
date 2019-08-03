#import all libraries
from telegram.ext import Updater, CommandHandler
import requests
import re

#access API and get the image url
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def doggo(bot, update):
    #Get image url
    url = get_url()
    #Get the recipient ID
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('891362789:AAFZZgY6BhSeRHUJx1jRRiFRrI-WJtCdrqU')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('doggo',doggo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
