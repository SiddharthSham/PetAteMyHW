import config

#This module is used for connecting to the Wolfram Alpha API
#It defines a function that passes the query via an URL
#returns data as gif/jpeg. Very successful in initial tests.

def query(query):
    #query = query[7:]                                                      #dormant function. Integration pending.
    question = query.replace(" ","+")
    return  "http://api.wolframalpha.com/v1/simple?appid={}&i=".format(config.APP_ID) + question + "&format=image"
    
