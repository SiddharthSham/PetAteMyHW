import logging
import wolfram, Wiki, config, chatter, OCR
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

#This is the main module which oversees the bot.
#API related functions are called seperately. *Only* functions directly affecting the bot are stored here.
#Fragile. Handle with care. :P

#TODO: Exception handling is to be added in all modules.
#TODO: Add OCR module

updater = Updater(token = config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

commands = ["wiki", "wolfram"]              #index of commands

"""Start of function definitions"""

def checker(bot, update):
    text = update.message.text              #gets the user input
    text = text.split(" ")[0]               #stores the first word of the input
    given = update.message.text
    if text in commands:                    #this block checks the command used and passes control accordingly
        if text == "wolfram":               
            bot.send_document(chat_id = update.message.chat_id, document = wolfram.query(given[8:]))
        else:
            bot.send_message(chat_id = update.message.chat_id, text = Wiki.wiki(given[5:]))
    else: 
        bot.send_message(chat_id = update.message.chat_id, text = chatter.chat(update.message.text))

def start(bot, update):                      #The user is greeted by this message. A quick start guide, in essence.
    bot.send_message(chat_id = update.message.chat_id, text="Hi! What can I do for you? Use these commands to talk to me:")
    bot.send_message(chat_id = update.message.chat_id, text="Start a sentence with \"wolfram\" to to get a mathematical or scientific answer")
    bot.send_message(chat_id = update.message.chat_id, text="Start a sentence with \"wiki\" to search Wikipedia for some information.")
    bot.send_message(chat_id = update.message.chat_id, text="...or we could just talk away our time, eh? ;)")

#def ocr(bot, update):                                          
#    bot.send_message(chat_id = update.message.chat_id, text = OCR.ocr(update.message.text))

"""End of function definitions"""

"""Start of handlers"""
query_handler = MessageHandler(Filters.text, checker)           #handles textual queries
dispatcher.add_handler(query_handler)

#ocr_handler = MessageHandler(Filters.photo, ocr)               #(theoretically)handles queries in the form of images 
#dispatcher.add_handler(ocr_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

"""End of handlers"""

updater.start_polling()
