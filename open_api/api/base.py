# -*- encoding: utf8 -*-
from ..model.base import BaseModel

__all__ = [
    "ApiBaseClass",
]


class ApiBaseClass(object):

    uri = ""

    def __init__(self, model=None):
        self._model = model

    def get_business_params(self):
        """
        获取业务参数
        :return:
        """
        return self._model.to_json if isinstance(self._model, BaseModel) else ""




