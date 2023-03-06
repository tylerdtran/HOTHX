from django.shortcuts import render
from django.views import generic
from django.db import models
from webscraper.models import Events

def save_function(event_list):
    print('starting save')
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
            print('failed at latest_event is none')
            print(e)
            break
    return print('finished')

# # replace the following line with the webscraper function
# save_function([{
# 'name': 'anameofanevent',
# 'link': 'https://volunteer.surfrider.org',
# 'start_time': '2021-09-25T09:00:00-07:00',
# 'end_time': '2021-09-25T12:00:00-07:00',
# 'location': 'San Diego, CA'
# }])

def home_page_view(request):
    context = {}
    context['events'] = Events.objects.all()
    return render(request, 'home.html', context)