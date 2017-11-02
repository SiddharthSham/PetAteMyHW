import config

#This module is used for calling the Wolfram Alpha API
#It defines a function that constructs an URL based on the query.
#NOTE: This module returns only the URL. This URL is passed in the bot.py file. Telegram Takes care of the rest.

def query(query):
    question = query.replace(" ","+")                   #plus encoding
    return  "http://api.wolframalpha.com/v1/simple?appid={}&i=".format(config.WOLFRAM) + question + "&format=image"
                                                        #returns ONLY the URL directly.
                                                        #Telegram's servers handle the requests by themselves for docs lesser than 20MB  
