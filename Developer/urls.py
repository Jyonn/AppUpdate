from django.conf.urls import url
from Developer.views import *

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
]
