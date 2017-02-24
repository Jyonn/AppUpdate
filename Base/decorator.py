from functools import wraps

from django.views.decorators import http

from Base.response import *

require_post = http.require_POST
require_get = http.require_GET


def require_params(need_params):
    """
    需要获取的参数是否在request.POST中存在
    """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            for need_param in need_params:
                if need_param not in request.POST:
                    return error_response(Error.REQUIRE_PARAM, append_msg=need_param)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def require_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.body:
            try:
                request.POST = json.loads(request.body.decode())
            except:
                pass
            return func(request, *args, **kwargs)
        else:
            return error_response(Error.REQUIRE_JSON)

    return wrapper


def decorator_generator(verify_func, error_id):
    """
    装饰器生成器
    """

    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if verify_func(request):
                return func(request, *args, **kwargs)
            return error_response(error_id)
        return wrapper
    return decorator


def require_login_func(request):
    if "isLogin" not in request.session or "uid" not in request.session:
        return False
    if request.session["isLogin"] is None or request.session["uid"] is None:
        return False
    return request.session["isLogin"]


require_login = decorator_generator(require_login_func, Error.NEED_LOGIN)
