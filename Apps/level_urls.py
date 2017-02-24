from django.conf.urls import url
from Apps.views import *
from Apps.developer_views import *


urlpatterns = [
    url(r'^create/$', create_level),
    url(r'^modify-info/$', modify_level_info),
    url(r'^get-all/$', get_levels),
]
