# -*- encoding: utf8 -*-
import json


class BaseModel(object):

    def field_check(self):
        """
        必填属性校验,返回bool
        :return:
        """
        raise NotImplementedError("U must verify the required fields, so please implement method: field_check()")

    def to_json(self):
        """
        将属性转换成json字符串
        :return:
        """
        self.field_check()

        return json.dumps(self.__dict__, separators=(",", ":")) if self.__dict__ else ""

    def to_dict(self):
        """
        将属性转化成dict
        :return:
        """
        self.field_check()

        return self.__dict__
