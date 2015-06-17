from django.conf.urls import patterns, url

from chat import views
from views import *
urlpatterns = patterns('',
        #url(r'^$', views.index, name='index'),
        url(r'^saverecord/$', saverecord , name = "saverecord"),

        #url(r'^long_poll/(?P<chat_room_id>\d+)/$', views.longpoll_chat_room, name='longpoll_chat_room'),
)
