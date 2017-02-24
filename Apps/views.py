from Base.decorator import *
from Base.common import *


@require_post
@require_json
@require_params(['appEnglishName', 'level'])
def get_latest_version(request):
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_version, ret_code = get_latest_version_func(apps, level)
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response(body=get_version_detail_func(o_version))


@require_post
@require_json
@require_params(['appEnglishName', 'level', 'version'])
def get_state(request):
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']
    version = request.POST['version']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    latest_version, ret_code = get_latest_version_func(apps, level)
    if ret_code != Error.OK:
        return error_response(ret_code)

    current_version, ret_code = get_version_func(apps, version)
    if ret_code != Error.OK:
        return error_response(ret_code)

    latest_version_detail = get_version_detail_func(latest_version)
    latest_version_detail["isLatest"] = (latest_version == current_version)

    return response(body=latest_version_detail)


@require_post
def get_apps(request):
    return response(body=get_app_list_func())


@require_post
@require_json
@require_params(['appEnglishName'])
def get_levels(request):
    app_english_name = request.POST['appEnglishName']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response(body=get_level_list_func(apps))


@require_post
@require_json
@require_params(['appEnglishName', 'level'])
def get_versions(request):
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response(body=get_version_list_func(apps, level))


@require_post
@require_json
@require_params(['appEnglishName', 'version'])
def get_exact_version(request):
    app_english_name = request.POST['appEnglishName']
    version = request.POST['version']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_version, ret_code = get_version_func(apps, version)
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response(body=get_version_detail_func(o_version, True))
