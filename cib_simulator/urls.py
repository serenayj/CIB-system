from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
from sampleapp.views import *

from views import *

admin.autodiscover()

urlpatterns = [

	url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', login_view),
    url(r'logout/$', logout_view),
    url(r'register/$', register),
    url(r'chat/', include('chat.urls')),
    url(r'login/chats', include('chat.urls')),
    #url("", include('django_socketio.urls')),
]
