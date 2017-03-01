from django.shortcuts import render

from Apps.views import get_level_list_func
from Base.common import get_app_list_func, get_apps_by_english_name_func, get_app_detail, get_latest_version_func, \
    get_version_detail_func
from Base.error import Error


def index(request):
    app_list = get_app_list_func()
    return render(request, "index.html", {'app_list': app_list})


def login(request, redirect):
    if redirect.find('redirect='):
        redirect = '/app/index/'
    else:
        redirect = redirect[9:]
    return render(request, "login.html", {'redirect': redirect})


def detail(request, app_english_name):
    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return render(request, "error.html")

    return_dict = dict(app_detail=get_app_detail(apps))
    levels = get_level_list_func(apps)
    versions = []
    for i, level in enumerate(levels):
        o_version, ret_code = get_latest_version_func(apps, level['level'], force_level=True)
        if o_version is not None:
            version_dict = get_version_detail_func(o_version, with_url=True)
            version_dict['offset'] = 0 if i % 2 == 0 else 4
            versions.append(version_dict)
    return_dict['version_list'] = versions
    return render(request, "detail.html", return_dict)
