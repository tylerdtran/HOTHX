# events model
# from .models import Events

# scraping tools
from bs4 import BeautifulSoup
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

SURFRIDER_URL = 'https://volunteer.surfrider.org'
DRIVER_PATH = "/Users/ajtadeo/chromedriver_mac64/chromedriver"

# This function scrapes the Surfrider Foundation website for events
def scrape_surfrider():
    e_list = []
    try:
        print('Starting the scraping tool')
        # set up options
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument("--disable-gpu")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')

        # set up driver
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options, chrome_options=chrome_options)
        driver.get(SURFRIDER_URL)

        # get 2 events from the page
        e = driver.find_element(By.CLASS_NAME, 'opportunityCard')
        e_list.append(scrape_event(e))
        e = e.find_element(By.XPATH, "//article/following-sibling::article")
        e_list.append(scrape_event(e))
    except Exception as err:
        print('The scraping job failed. See exception:')
        print(err)
    print(e_list)

def scrape_event(event):
    link = event.find_element(By.TAG_NAME, "a").get_attribute("href")
    name = event.find_element(By.TAG_NAME, "h2").text
    organization = event.find_element(By.TAG_NAME, "h3").text

    dateTime_and_location = event.find_elements(By.TAG_NAME, "li")
    date_and_time = dateTime_and_location[0].find_element(By.CLASS_NAME, "timeDetails").text
    location = dateTime_and_location[1].text

    result = {
        "name": name,
        "organization": organization,
        "link": link,
        "date_and_time": date_and_time,
        "location": location
    }

    return result

# This function takes a list of JSON events and loads them into the database
def save_function(event_list):
    print('starting')
    new_count = 0

    for event in event_list:
        try:
            Events.objects.create(
                name=event['name'],
                link=event['link'],
                start_time=event['start_time'],
                end_time=event['end_time'],
                location=event['location']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_event is none, but its OK')
            print(e)
            break
    return print('finished')

if __main__ == '__main__':
    scrape_surfrider()