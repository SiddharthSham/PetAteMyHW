import requests, json
#from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

def query(query):
    question = query.replace(" ","+")
    url = "http://api.wolframalpha.com/v1/simple?appid=APP_ID=" + question + "&format=image"
    return url
