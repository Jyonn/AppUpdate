class Error:
    NOT_JPEG_LOGO = 2021
    LOGO_SIZE = 2020
    NOT_FOUND_LOGO = 2019
    ILLEGAL_DESCRIPTION_LENGTH = 2018
    ILLEGAL_NOTE_LENGTH = 2017
    ILLEGAL_APP_NAME_LENGTH = 2016
    ILLEGAL_APP_ENGLISH_NAME_LENGTH = 2015
    VERSION_NOT_ALIVE = 2014
    EXISTED_VERSION = 2013
    APPS_NOT_ALIVE = 2012
    ERROR_GET_HASH = 2011
    ILLEGAL_VERSION = 2010
    ILLEGAL_LEVEL = 2009
    ILLEGAL_NOTE = 2008
    ILLEGAL_APP_NAME = 2007
    ILLEGAL_APP_ENGLISH_NAME = 2006
    NOT_FOUND_FILE = 2005
    ADD_VERSION_FAILED = 2005
    ADD_LEVEL_FAILED = 2004
    ADD_APPS_FAILED = 2003
    NOT_FOUND_VERSION = 2002
    NOT_FOUND_LEVEL = 2001
    NOT_FOUND_APPS = 2000
    NEED_LOGIN = 1003
    REQUIRE_JSON = 1002
    REQUIRE_PARAM = 1001
    NOT_FOUND_ERROR = 1000
    OK = 0

    ERROR_DICT = [
        (NOT_JPEG_LOGO, "错误的图标格式"),
        (LOGO_SIZE, "图标超过最大上传限度"),
        (NOT_FOUND_LOGO, "不存在的应用图标"),
        (ILLEGAL_DESCRIPTION_LENGTH, "非法版本描述长度"),
        (ILLEGAL_NOTE_LENGTH, "非法备注长度"),
        (ILLEGAL_APP_NAME_LENGTH, "非法应用名长度"),
        (ILLEGAL_APP_ENGLISH_NAME_LENGTH, "非法应用名英文长度"),
        (VERSION_NOT_ALIVE, "该版本已被下架"),
        (EXISTED_VERSION, "已存在的版本号"),
        (APPS_NOT_ALIVE, "应用已被下架，不支持服务"),
        (ERROR_GET_HASH, "获取文件哈希失败"),
        (ILLEGAL_VERSION, "非法版本号"),
        (ILLEGAL_LEVEL, "非法更新等级"),
        (ILLEGAL_NOTE, "非法备注"),
        (ILLEGAL_APP_NAME, "非法应用名"),
        (ILLEGAL_APP_ENGLISH_NAME, "非法应用英文名"),
        (NOT_FOUND_FILE, "不存在的应用文件"),
        (ADD_VERSION_FAILED, "添加新版本失败"),
        (ADD_LEVEL_FAILED, "添加更新等级失败"),
        (ADD_APPS_FAILED, "添加应用失败"),
        (NOT_FOUND_VERSION, "不存在的版本"),
        (NOT_FOUND_LEVEL, "不存在的更新等级"),
        (NOT_FOUND_APPS, "不存在的应用"),

        (NEED_LOGIN, "需要登录"),
        (REQUIRE_JSON, "需要JSON数据"),
        (REQUIRE_PARAM, "缺少参数"),
        (NOT_FOUND_ERROR, "不存在的错误"),
        (OK, "没有错误"),
    ]
