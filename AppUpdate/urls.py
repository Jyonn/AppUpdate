"""AppUpdate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import static, url

from AppUpdate.settings import ICO_URL
from Apps.views import *
from Apps.admin_views import *
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^app/create/$', create_apps),
    url(r'^app/modify-info/$', modify_apps_info),
    url(r'^app/modify-logo/$', modify_apps_logo),
    url(r'^app/set-dead/$', set_apps_dead),
    url(r'^app/get-all/$', get_apps),

    url(r'^level/create/$', create_level),
    url(r'^level/modify-info/$', modify_level_info),
    url(r'^level/get-all/$', get_levels),

    url(r'^version/create/$', create_version),
    url(r'^version/set-dead/$', set_version_dead),
    url(r'^version/latest/$', get_latest_version),
    url(r'^version/get-all/$', get_versions),
    url(r'^version/get-exact/$', get_exact_version),

    url(r'^get-state/$', get_state),
]

urlpatterns += static.static('favicon.ico', document_root=ICO_URL)
