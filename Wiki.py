import json, requests

#This module handles Wikipedia queries.
#It will return the summary of a topic provided on its respective page.
#NOTE: The query is successful only if the query exactly matches the title of the Wikipedia page.

def wiki(query):
    #query = query[4:]                                                     #dormant function. New features coming soon.
    query = query.replace(" ", "%20")
    url = "https://en.wikipedia.org/w/api.php?format=json&utf8=&action=query&prop=extracts&exintro=&explaintext=&titles=" + query
    response = requests.get(url)
    content = json.loads(response.content.decode("utf-8"))
    n = str(content['query']['pages'].keys())[12:-3]
    return content['query']['pages'][n]['extract']
