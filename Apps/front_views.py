from django.http import HttpResponseRedirect
from django.shortcuts import render

from Base.common import *
from Base.decorator import require_login_func
from Base.error import Error


def index(request):
    app_list = []
    apps = Apps.objects.filter(isAlive=True)
    for app in apps:
        app_detail = get_app_detail(app)
        o_version, ret_code = get_latest_version_func(app, 0, force_level=True)
        if ret_code == Error.OK:
            app_detail['latest'] = get_version_detail_func(o_version, with_url=True)
        app_list.append(app_detail)
    return render(request, "index.html", {'app_list': app_list})


def login(request, redirect):
    if require_login_func(request):
        return HttpResponseRedirect('/app/index/')
    if redirect.find('redirect='):
        redirect = '/app/index/'
    else:
        redirect = redirect[9:]
    return render(request, "login.html", {'redirect': redirect})


def detail(request, app_english_name):
    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return render(request, "error.html")

    return_dict = dict(app=get_app_detail(apps))
    levels = get_level_list_func(apps)
    for level in levels:
        o_version, ret_code = get_latest_version_func(apps, level['level'], force_level=True)
        if o_version is not None:
            level['latest'] = get_version_detail_func(o_version, with_url=True)
        # level['all'] = get_version_list_func(apps, level['level'])
    return_dict['levels'] = levels
    return render(request, "detail.html", return_dict)
