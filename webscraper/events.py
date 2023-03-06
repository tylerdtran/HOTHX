# events model
# from .models import Events

# scraping tools
from bs4 import BeautifulSoup
import json
from datetime import datetime
from requests_html import HTMLSession

SURFRIDER_URL = 'https://volunteer.surfrider.org'

# This function scrapes the Surfrider Foundation website for events
def scrape_surfrider():
    article_list = []
    try:
        # print('Starting the scraping tool')

        # create an HTML session
        session = HTMLSession()

        # send a GET request to the page
        response = session.get(SURFRIDER_URL)

        # render the JavaScript on the page
        response.html.render()

        # extract the content you want using Beautiful Soup
        soup = BeautifulSoup(response.html.html, 'html.parser')
        
        # sample Event in json format
        sample_event = {
            'name': 'Surfsample Foundation - San Diego Chapter',
            'link': 'https://volunteer.surfrider.org/index.cfm?fuseaction=donate.event&eventID=1000',
            'start_time': '2021-09-25T09:00:00-07:00',
            'end_time': '2021-09-25T12:00:00-07:00',
            'location': 'San Diego, CA'
        }
        
        bad_sample_event = {
            "component": "event",
            "title": "Beach Cleanup",
            "location": "Long Beach, CA",
            "date": "June 21, 2023",
            "time": "9:00am",
            "organization": "Long Beach Surfrider"
        }

        # THE REST OF THIS FUNCTION DOES NOT WORK

        # # execute my request, parse the data using XML parser in BS4
        # soup = BeautifulSoup(r.content, features='xml')
        # # select only the "items" I want from the data
        # articles = soup.findAll('item')
    
        # # for each "item" I want, parse it into a list
        # for a in articles:
        #     title = a.find('title').text
        #     link = a.find('link').text
        #     published_wrong = a.find('pubDate').text
        #     published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        #     # print(published, published_wrong) # checking correct date format
        #     # create an "article" object with the data
        #     # from each "item"
        #     article = {
        #         'title': title,
        #         'link': link,
        #         'published': published,
        #         'source': 'HackerNews RSS'
        #     }
        #     # append my "article_list" with each "article" object
        #     article_list.append(article)
        #     print('Finished scraping the articles')
    
        #     # after the loop, dump my saved objects into a .txt file
            return save_function([bad_sample_event])
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

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
                location = event['location']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_event is none, but its OK')
            print(e)
            break
    return print('finished')

if __main__ == '__main__':
    scrape_surfrider()