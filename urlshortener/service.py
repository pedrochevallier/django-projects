import requests
import environ
from websitecategorization  import *


env = environ.Env()
environ.Env.read_env()


def url_check(url):
    check = url.split(":")
    if ((check[0] == 'http') or (check[0] == 'https')):
        return url
    else:
        url = 'http://' + url
        return url

def categorize_url(url):
    category = None
    api = env('WHOISXML_KEY')
    client = Client(api)
    try:
        response = client.data(url)
        if response.website_responded:
            for cat in response.categories:
                if cat.tier1:
                    category = cat.tier1.id
            return category
        else:
            return category
    except:
        return category
