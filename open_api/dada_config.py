# -*- encoding: utf8 -*-

"""
接口配置项
部分配置申请入口:http://newopen.imdada.cn/#/page/guide?_k=j74tr1
"""


class BaseConfig(object):

    # 开发者在线上或测试环境的app_key与app_secret是一样
    APP_KEY = "dada7c9572fb300cc35"
    APP_SECRET = "69543f1940c374d176abdd4d8be8eaa8"


class QAConfig(BaseConfig):

    HOST = "http://127.0.0.1:8089"
    SOURCE_ID = 73758


class OnlineConfig(BaseConfig):

    HOST = ""
    SOURCE_ID = 0

