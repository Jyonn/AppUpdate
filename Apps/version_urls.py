from django.conf.urls import url
from Apps.views import *
from Apps.developer_views import *


urlpatterns = [
    url(r'^create/$', create_version),
    url(r'^set-dead/$', set_version_dead),
    url(r'^latest/$', get_latest_version),
    url(r'^get-all/$', get_versions),
    url(r'^get-exact/$', get_exact_version),
    url(r'^get-state/$', get_state),
    url(r'^exist/$', exist),
]
