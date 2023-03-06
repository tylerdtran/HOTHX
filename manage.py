#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webscraperevents

scrape_surfrider()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hothx.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


## Scrape Tool ##

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
    save_function(e_list)

def scrape_event(event):
    link = event.find_element(By.TAG_NAME, "a").get_attribute("href")
    eventname = event.find_element(By.TAG_NAME, "h2").text
    organization = event.find_element(By.TAG_NAME, "h3").text

    dateTime_and_location = event.find_elements(By.TAG_NAME, "li")
    date_and_time = dateTime_and_location[0].find_element(By.CLASS_NAME, "timeDetails").text
    location = dateTime_and_location[1].text

    result = {
        "eventname": eventname,
        "organization": organization,
        "link": link,
        "date_and_time": date_and_time,
        "location": location,
        "placeid": placeid
    }

    return result

# This function takes a list of JSON events and loads them into the database
def save_function(event_list):
    print('starting save')
    new_count = 0

    for event in event_list:
        try:
            Events.objects.create(
                eventname = event['eventname'],
                organization = event['organization'],
                link = event['link'],
                date_and_time = event['date_and_time'],
                location = event['location'],
                placeid = event['placeid']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_event is none')
            print(e)
            break
    return print('finished')