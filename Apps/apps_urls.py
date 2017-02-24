from django.conf.urls import url, static

from AppUpdate.settings import APP_URL, LOGO_URL
from Apps import views, developer_views, front_views

urlpatterns = [
    url(r'^create/$', developer_views.create_apps),
    url(r'^modify-info/$', developer_views.modify_apps_info),
    url(r'^modify-logo/$', developer_views.modify_apps_logo),
    url(r'^set-dead/$', developer_views.set_apps_dead),
    url(r'^get-all/$', views.get_apps),
] + [
    url(r'^index/$', front_views.index),
]

urlpatterns += static.static('logo/', document_root=LOGO_URL)
urlpatterns += static.static('dl/', document_root=APP_URL)
