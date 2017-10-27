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

#uncomment the following lines to enable the Wikipedia module. NOTE: It cannot be run alongside the Wolfram module.
#SUGGESTED: Add a filter to handle queries starting with "wiki" seperately from normal queries.

#def wikipedia(bot, update):
#   bot.send_message(chat_id = update.message.chat_id, text = Wiki.wiki(update.message.text))

#wikipedia_handler = MessageHandler(Filters.text, wikipedia)
#dispatcher.add_handler(wikipedia_handler)

query_handler = MessageHandler(Filters.text, query)
dispatcher.add_handler(query_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
