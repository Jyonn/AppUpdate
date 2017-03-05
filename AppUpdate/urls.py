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
from django.conf.urls import url, static, include
from AppUpdate.settings import STATIC_DIR_URL

from Developer.views import *
from Apps.front_views import index

urlpatterns = [
    url(r'^app/', include('Apps.apps_urls')),
    url(r'^level/', include('Apps.level_urls')),
    url(r'^version/', include('Apps.version_urls')),

    url(r'^developer/', include('Developer.urls')),
] + [
    url(r'^$', index),
]

urlpatterns += static.static('/', document_root=STATIC_DIR_URL)
