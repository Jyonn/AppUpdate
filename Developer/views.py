from Base.decorator import *
from Base.common import *
from Developer.models import Developer


@require_post
@require_json
@require_params(['username', 'password'])
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        developer = Developer.objects.get(username=username)
        if developer.isFrozen:
            return error_response(Error.FROZEN_USER)
        if developer.check_password(password):
            login_to_session(request, developer)
            return response()
        else:
            return error_response(Error.ERROR_PASSWORD)
    except:
        return error_response(Error.NOT_FOUND_USERNAME)


@require_post
def logout(request):
    request.session["isLogin"] = None
    request.session["uid"] = None
    return response()


@require_post
@require_json
@require_params(["old_password", "new_password"])
@require_login
def change_password(request):
    """
    修改用户密码
    """
    old_password = request.POST["old_password"]
    new_password = request.POST["new_password"]
    developer = get_user_from_session(request)
    if developer is None:
        return error_response(Error.NEED_LOGIN)
    if not developer.check_password(old_password):
        return error_response(Error.ERROR_PASSWORD)
    developer.set_password(new_password)
    developer.save()
    return response()
