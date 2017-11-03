import logging                      #imports logging module

import chatter                      #this section imports the other files required for the various features of this bot.
import config
import Wiki
import wolfram
import OCR
                                  
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
#This line imports the telegram wrapper, and makes the functions usable. Three cheers for wrappers and APIs!


#This is the main module which oversees the bot.
#API related functions are called seperately. *Only* functions directly affecting the bot are stored here.



updater = Updater(token = config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

commands = ["wiki", "wolfram", "Wolfram", "Wiki"]              #list of commands available to user.



#Start of function definitions

def checker(bot, update):
    text = update.message.text              #gets the user input
    text = text.split(" ")[0]               #stores the first word of the input
    given = update.message.text

    if text in commands:                    #this block checks the command used and passes control accordingly
        if text == "wolfram" or text == "Wolfram":
            try:               
                bot.send_document(chat_id = update.message.chat_id, document = wolfram.query(given[8:]))
            except:
                bot.send_message(chat_id = update.message.chat_id, text = "Couldn't find an answer to your question. Something easier, please?")

        elif text == "wiki" or text == "Wiki":
            try:
                bot.send_message(chat_id = update.message.chat_id, text = Wiki.wiki(given[5:]))
            except:
                bot.send_message(chat_id = update.message.chat_id, text = "Sorry, couldn't get you. Note that the query has to exactly match the Wikipedia article title. Please check your capitalisation.")
            
    else:
        try: 
            bot.send_message(chat_id = update.message.chat_id, text = chatter.chat(update.message.text))
        except:
            bot.send_message(chat_id = update.message.chat_id, text = "Something went wrong. Have a cookie while my boss fixes me. And give him one too. ;)")


def start(bot, update):                                 #The user is greeted by this message. A quick start guide, in essence.
    user = update.message.from_user            
    bot.send_message(chat_id = update.message.chat_id, text="Hi! What can I do for you, %s? Use these commands to talk to me:"%user.first_name)
    bot.send_message(chat_id = update.message.chat_id, text="Start a sentence with \"Wolfram\" to to get a mathematical or scientific answer")
    bot.send_message(chat_id = update.message.chat_id, text="Start a sentence with \"Wiki\" to search Wikipedia for some information. P.S.: Ensure your capitalisation is correct.")
    bot.send_message(chat_id = update.message.chat_id, text="...or we could just talk away our time, eh? ;)")

def img(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "Images are not supported *yet*.")
    bot.send_message(chat_id = update.message.chat_id, text = "But the future is looking bright!")

"""
def ocr(bot, update):                                   #experimental feature. Runs on magic and stardust. Predictably, doesn't work. :/
    try:                                          
        bot.send_message(chat_id = update.message.chat_id, text = OCR.message(bot, update))
        #bot.send_document(chat_id = update.message.chat_id, document = wolfram.query(OCR.ocr(update.message.text)))        #Passes queries obtained from OCR directly into wolfram alpha API.
    except:
        bot.send_message(chat_id = update.message.chat_id, text = "I'm not ready to show you my full potential yet. You may shut me down. Until then, muauauhahahhahah!!!")
"""
#End of function definitions



#Start of handlers

query_handler = MessageHandler(Filters.text, checker)          #handles textual queries
dispatcher.add_handler(query_handler)                          #Passes control to the main control block


ocr_handler = MessageHandler(Filters.photo, img)               #handles queries in the form of images 
dispatcher.add_handler(ocr_handler)                            #and passes control to img module. Was designed for OCR module.




start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#End of handlers


updater.start_polling()                                         #starts long polling
