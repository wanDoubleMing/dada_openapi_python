# -*- encoding: utf8 -*-
import json

CALL_EXCEPT_CODE = -2
CALL_EXCEPT_MSG = "请求异常,请检查网络情况"
SUCCESS = "success"
FAIL = "fail"

__all__ = [
    "DadaRpcResponse",
]


class DadaRpcResponse(object):

    def __init__(self):
        """
        返回的结构体
        :return:
        """
        self.status = None
        self.code = None
        self.msg = None
        self.result = None

    @staticmethod
    def parse_resp_content(resp_content):
        """
        解析json字符串
        :return:
        """
        resp = DadaRpcResponse()
        content = json.loads(resp_content)
        for key, value in content.iteritems():
            if value:
                setattr(resp, key, value)

        return resp

    @staticmethod
    def call_except():
        resp = DadaRpcResponse()
        resp.code = CALL_EXCEPT_CODE
        resp.msg = CALL_EXCEPT_MSG
        resp.status = FAIL
        return resp

    def to_string(self):
        """
        :return:
        """
        return json.dumps(self.__dict__)