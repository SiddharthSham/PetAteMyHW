import requests, json

def query(query):
    question = query.replace(" ","+")
    url = "http://api.wolframalpha.com/v1/simple?appid=APP_ID=" + question + "&format=image"
    return url
