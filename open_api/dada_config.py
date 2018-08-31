# -*- encoding: utf8 -*-

"""
接口配置项
部分配置申请入口:http://newopen.imdada.cn/#/page/guide?_k=j74tr1
"""


class BaseConfig(object):

    # 开发者在线上或测试环境的app_key与app_secret是一样
    APP_KEY = ""
    APP_SECRET = ""
    HOST = ""

    @classmethod
    def init_check(cls):
        if not cls.APP_KEY:
            raise ValueError("APP_KEY can not be empty, please assign a value")

        if not cls.APP_SECRET:
            raise ValueError("APP_SECRET can not be empty, please assign a value")

        if not cls.HOST:
            raise ValueError("host can not be empty, please assign a value")

        return True

class QAConfig(BaseConfig):

    HOST = "http://newopen.qa.imdada.cn"
    SOURCE_ID = "73758"


class OnlineConfig(BaseConfig):

    HOST = "https://newopen.imdada.cn"
    SOURCE_ID = ""

