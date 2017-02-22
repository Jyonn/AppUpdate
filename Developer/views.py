from Base.decorator import *
from Base.common import *


@require_post
@require_json
@require_params(['username', 'password'])
def login(request):
    developer = De
    return response()