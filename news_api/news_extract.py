import requests
import sys

from config import *

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&' + 'apiKey=' + str(news_api_token))

response = requests.get(url)

print(response.json())