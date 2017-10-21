import logging
import wolfram, Wiki
import requests
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

updater = Updater(token = congig.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Hi! What can I do for you?")

def query(bot, update):
   bot.send_document(chat_id = update.message.chat_id, document = wolfram.query(update.message.text))

#def wikipedia(bot, update):
#   bot.send_message(chat_id = update.message.chat_id, text = Wiki.wiki(update.message.text))

query_handler = MessageHandler(Filters.text, query)
dispatcher.add_handler(query_handler)

#wikipedia_handler = MessageHandler(Filters.text, wikipedia)
#dispatcher.add_handler(wikipedia_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
