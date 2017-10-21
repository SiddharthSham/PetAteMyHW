import requests, json

def wiki(query):
    query = query.replace(" ", "%20")
    url = "https://en.wikipedia.org/w/api.php?format=json&utf8=&action=query&prop=extracts&exintro=&explaintext=&titles=" + query
    response = requests.get(url)
    content = json.loads(response.content.decode("utf-8"))
    n = str(content['query']['pages'].keys())
    n = n[12:-3]
    return (content['query']['pages'][n]['extract'])