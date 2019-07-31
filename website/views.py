from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta

from .models import *
from .utils import Calendar


def home(request):
    return render(request, 'website/home.html',)

def results(request):
    return render(request, 'website/results.html')

def learntoswim(request):
    return render(request, 'website/learntoswim.html')

def contact(request):
    return render(request, 'website/contact.html')   

def news(request):
    return render(request, 'website/news.html')   

def services(request):
    return render(request, 'website/services.html') 

def findclub(request):
    return render(request, 'website/findclub.html') 

def history(request):
    return render(request, 'website/history.html') 

def committee(request):
    return render(request, 'website/committee.html')

def gallery(request):
    return render(request, 'website/gallery.html')

def categories(request):
    return render(request, 'website/categories.html')

def events(request):
    return render(request, 'website/events.html')

def video(request):
    return render(request, 'website/video.html')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'website/calendar.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))
        

      

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

