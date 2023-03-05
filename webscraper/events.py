# events model
from .models import Events

# scraping
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import lxml

SURFRIDER_URL = 'https://volunteer.surfrider.org'

# This function scrapes the Surfrider Foundation website for events
# def scrape_surfrider():
#     article_list = []
#     try:
#         print('Starting the scraping tool')
#         # execute my request, parse the data using XML
#         # parser in BS4
#         r = requests.get(SURFRIDER_URL)
#         soup = BeautifulSoup(r.content, features='xml')
#         # select only the "items" I want from the data
#         articles = soup.findAll('item')
    
#         # for each "item" I want, parse it into a list
#         for a in articles:
#             title = a.find('title').text
#             link = a.find('link').text
#             published_wrong = a.find('pubDate').text
#             published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
#             # print(published, published_wrong) # checking correct date format
#             # create an "article" object with the data
#             # from each "item"
#             article = {
#                 'title': title,
#                 'link': link,
#                 'published': published,
#                 'source': 'HackerNews RSS'
#             }
#             # append my "article_list" with each "article" object
#             article_list.append(article)
#             print('Finished scraping the articles')
    
#             # after the loop, dump my saved objects into a .txt file
#             return save_function(article_list)
#     except Exception as e:
#         print('The scraping job failed. See exception:')
#         print(e)

# This function takes a list of JSON events and loads them into the database
def save_function(event_list):
    print('starting')
    new_count = 0

    for event in event_list:
        try:
            Events.objects.create(
                name = event['name'],
                link = event['link'],
                start_time = event['start_time'],
                end_time = event['end_time'],
                created_at = event['created_at'],
                updated_at = event['updated_at'],
                location = event['location']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_event is none')
            print(e)
            break
    return print('finished')