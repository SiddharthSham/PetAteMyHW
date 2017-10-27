from chatterbot import ChatBot
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import config
import logging

updater = Updater(token = config.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Hi! Try talking to me!")

chatbot = ChatBot('SidiousBot', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

chatbot.train('chatterbot.corpus.english')
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")

def chatter(bot,update):
    send = str(chatbot.get_response(update.message.text))
    bot.send_message(chat_id = update.message.chat_id, text = send)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

query_handler = MessageHandler(Filters.text, chatter)
dispatcher.add_handler(query_handler)

updater.start_polling()