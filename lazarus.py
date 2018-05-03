import telegram
from os import environ

#Pulls Telegram Bot API Access Token from my Bash environment variables
bot=telegram.Bot(token=environ["TELEGRAMBOTTOKEN"])

#Pulls a chat ID from my Bash environment variables
chat_id = environ["CHAT"]

while True:
    msg = input(">")
    bot.send_message(chat_id, text=msg)
