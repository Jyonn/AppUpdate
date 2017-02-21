from Base.decorator import *
from Base.common import *


@require_post
@require_json
@require_params(['appName', 'appEnglishName'])
def create_apps(request):
    app_name = request.POST['appName']
    app_english_name = request.POST['appEnglishName']

    apps, ret_code = create_app_func(app_name, app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_level, ret_code = create_level_func(apps, 0, '默认')
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response()


@require_post
@require_json
@require_params(['appName', 'appEnglishName'])
def modify_apps_info(request):
    app_name = request.POST['appName']
    app_english_name = request.POST['appEnglishName']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    if not is_legal_string(app_name):
        return error_response(Error.ILLEGAL_APP_NAME)

    apps.appName = app_name
    apps.save()
    return response()


@require_post
@require_json
@require_params(['appEnglishName', 'level', 'note'])
def create_level(request):
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']
    note = request.POST['note']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_level, ret_code = create_level_func(apps, level, note)
    if ret_code != Error.OK:
        return error_response(ret_code)

    return response()


@require_post
@require_json
@require_params(['appEnglishName', 'level', 'note'])
def modify_level_info(request):
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']
    note = request.POST['note']

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_level, ret_code = get_level_func(apps, level)
    if ret_code != Error.OK:
        return error_response(ret_code)

    if not is_legal_string(note):
        return error_response(Error.ILLEGAL_NOTE)

    if not is_legal_length(level):
        return error_response(Error.ILLEGAL_LEVEL)

    o_level.level = level
    o_level.note = note
    o_level.save()
    return response()


@require_post
@require_json
@require_params(['appEnglishName', 'level', 'version', 'descriptionEncoded'])
def create_version(request):
    if request.FILES.get("appFile") is None:
        return error_response(Error.NOT_FOUND_FILE)
    app_english_name = request.POST['appEnglishName']
    level = request.POST['level']
    version = request.POST['version']
    description_encoded = request.POST['descriptionEncoded']

    if not is_legal_length(description_encoded, string_max=Version.C['descriptionEncodedLength']):
        return error_response(Error.ILLEGAL_DESCRIPTION_LENGTH)

    matched = re.search('^([a-zA-Z0-9_.\s]+)$', version)
    if matched is None:
        return error_response(Error.ILLEGAL_VERSION)

    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_version, ret_code = get_version_func(apps, version)
    if ret_code == Error.OK:
        return error_response(Error.EXISTED_VERSION)

    save_file = request.FILES.get("appFile")
    str_name = save_file.name
    ext_name = "" if str_name.find(".") == -1 else "." + str_name.split(".")[-1]
    file_name = app_english_name+'_'+version+ext_name[:8]
    file_path = os.path.join(APP_URL, app_english_name)
    file_path = os.path.join(file_path, file_name)
    with open(file_path, "wb+") as f:
        for chunk in save_file.chunks():
            f.write(chunk)
        f.close()
    md5, sha1 = get_file_hash(file_path)
    if md5 is None or sha1 is None:
        return error_response(Error.ERROR_GET_HASH)

    o_version, ret_code = create_version_func(apps, level, version, file_name, md5, sha1, description_encoded)
    if ret_code != Error.OK:
        return error_response(ret_code)
    return response()


@require_post
@require_json
@require_params(['appEnglishName'])
def set_apps_dead(request):
    app_english_name = request.POST['appEnglishName']
    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    if not apps.isAlive:
        return error_response(Error.APPS_NOT_ALIVE)

    apps.isAlive = False
    apps.save()
    return response()


@require_post
@require_json
@require_params(['appEnglishName', 'version'])
def set_version_dead(request):
    app_english_name = request.POST['appEnglishName']
    version = request.POST['version']
    apps, ret_code = get_apps_by_english_name_func(app_english_name)
    if ret_code != Error.OK:
        return error_response(ret_code)

    o_version, ret_code = get_version_func(apps, version)
    if ret_code != Error.OK:
        return error_response(Error.NOT_FOUND_VERSION)

    if not o_version.isAlive:
        return error_response(Error.VERSION_NOT_ALIVE)

    o_version.isAlive = False
    o_version.save()

    return response()
