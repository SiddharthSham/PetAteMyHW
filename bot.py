import logging
import wolfram, Wiki, config, chatter
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
#from chatterbot.filters import filter

#This is the main module which oversees the bot.
#All controls for activating/deactivating bot features are stored here
#Fragile. Handle with care.

#NOTE: Exception handling is to be added in all modules.

updater = Updater(token = config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Hi! What can I do for you")

def query(bot, update):
   bot.send_document(chat_id = update.message.chat_id, document = wolfram.query(update.message.text))

#uncomment the following lines to enable Wikipedia/Chatting functions.
#NOTE: Enable only ONE function at a time. Multiple functions will not work simultaneously.
#SUGGESTED: Write a filter to identify wolfram/wiki queries and handle them separately.

#def wikipedia(bot, update):
#    bot.send_message(chat_id = update.message.chat_id, text = Wiki.wiki(update.message.text))

#def chatter(bot, update):
#    bot.send_message(chat_id = update.message.chat_id, text = chatter.chat(update.message.text))

wolfram_handler = MessageHandler(Filters.text, query)
dispatcher.add_handler(wolfram_handler)

#wikipedia_handler = MessageHandler(filter.statement_response_list_contains("wiki"), wikipedia)
#dispatcher.add_handler(wikipedia_handler)

#chatter_handler = MessageHandler(Filters.text, chatter)
#dispatcher.add_handler(chatter_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
