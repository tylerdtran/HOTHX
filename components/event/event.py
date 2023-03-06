from django_components import component

@component.register("event")
class Event(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "event/event.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(name, link, start_time, end_time, location):
        print("HERE")
        return {
            "name": name,
            "link": link,
            "start_time": start_time,
            "end_time": end_time,
            "location": location,
            # "url": url
        }

    class Media:
        css = "event/event.css"
        # js = "calendar/calendar.js"