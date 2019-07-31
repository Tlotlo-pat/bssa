from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'^results/$', views.results, name='results'),
    path(r'^learntoswim/$', views.learntoswim, name='learntoswim'),
    path(r'^contact/$', views.contact, name='contact'),
    path(r'^news/$', views.news, name='news'),
    path(r'^services/$', views.services, name='services'),
    path(r'^findclub/$', views.findclub, name='findclub'),
    path(r'^history/$', views.history, name='history'),
    path(r'^committee/$', views.committee, name='committee'),
    path(r'^gallery/$', views.gallery, name='gallery'),
    path(r'^categories/$', views.categories, name='categories'),
    path(r'^events/$', views.events, name='events'),
    path(r'^video/$', views.video, name='video'),
    path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]


