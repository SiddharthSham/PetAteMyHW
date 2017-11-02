import json
import requests

#This module handles Wikipedia queries.
#It will return the summary of a topic provided on its respective page.
#NOTE: The query is successful only if the query exactly matches the title of the Wikipedia page.

def wiki(query):
    query = query.replace(" ", "%20")                              #performs percentage encoding
    url = "https://en.wikipedia.org/w/api.php?format=json&utf8=&action=query&prop=extracts&exintro=&explaintext=&titles=" + query
                                                                   #constructs the URL gor calling the API
    response = requests.get(url)                                   #posts a request to the constructed URL
    content = json.loads(response.content.decode("utf-8"))         #stores server response as JSON data
    n = str(content['query']['pages'].keys())[12:-3]               #Finds the requisite key. Quirk of the Wikimedia API.
    return  content['query']['pages'][n]['extract']                #Finally, returns the contents we want. Yay!
