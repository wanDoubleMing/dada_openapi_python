# -*- encoding: utf8 -*-
import hashlib
import requests
import json
import time
from .dada_response import DadaRpcResponse

__all__ = [
    "DadaApiClient",
]


class DadaApiClient(object):

    def __init__(self, client_config):
        """
        client_config 配置信息
        :param client_config:
        :return:
        """
        self.__client_config = client_config

    def do_rpc(self, api):
        """
        rpc请求
        :return:
        """
        headers = {'content-type': 'application/json'}

        url = self.__get_request_url(api)
        params = self.__get_request_params(api)
        try:
            resp = requests.post(url, data=json.dumps(params, separators=(",", ":")), headers=headers)
            if resp and resp.content:
                result = DadaRpcResponse.parse_resp_content(resp.content)
            else:
                result = DadaRpcResponse.call_except()

        except Exception as e:
            print "client do_rpc except: %s" % e.message
            result = DadaRpcResponse.call_except()

        return result

    def __get_request_url(self, api):
        """
        获取请求的url地址
        内部方法
        :param api:
        :return:
        """
        url = "{host}{uri}".format(host=self.__client_config.HOST, uri=api.uri)
        return url

    def __get_request_params(self, api):
        """
        准备请求参数
        内部方法
        :param api: 接口类
        :return:
        """
        common_params = self.__get_sign_params(api)
        signature = self.__make_sign(common_params)
        common_params["signature"] = signature
        return common_params


    def __get_sign_params(self, api):
        """
        获取签名参数
        内部方法
        :return:
        """
        sign_params = dict()
        sign_params["app_key"] = self.__client_config.APP_KEY
        sign_params["timestamp"] = int(time.time())
        sign_params["format"] = "json"
        sign_params["v"] = "1.0"
        sign_params["source_id"] = self.__client_config.SOURCE_ID
        sign_params["body"] = api.get_business_params()
        return sign_params

    def __make_sign(self, params):
        """
        签名
        内部方法
        :param params:
        :return:
        """
        sort_list = sorted(params.iteritems(), key=lambda x: x[0])

        sign_str = ""
        for ele in sort_list:
            sign_str += "%s%s" % (ele[0], ele[-1])

        sign_str = self.__client_config.APP_SECRET + sign_str + self.__client_config.APP_SECRET
        sign = hashlib.md5(sign_str).hexdigest()

        return sign.upper()

