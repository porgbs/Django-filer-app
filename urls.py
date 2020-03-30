from django.conf.urls import url, include
from django.contrib import admin
from .api import *
#
urlpatterns = [
    url(r'^api/folder/$', Folderlist.as_view(), name='folder'),
    url(r'^api/folder/(?P<id>\d+)/$', Folderlist.as_view(), name='folder'),
    url(r'^api/video/$', Videolist.as_view(), name='video'),
    url(r'^api/video/(?P<id>\d+)/$', Videolist.as_view(), name='video'),
    url(r'^api/image/$', Imagelist.as_view(), name='image'),
    url(r'^api/image/(?P<id>\d+)/$', Imagelist.as_view(), name='image'),
]