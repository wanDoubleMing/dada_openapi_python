# -*- encoding: utf8 -*-
__author__ = 'wan'

from .base import ApiBaseClass
from .urls import ORDER_CITY_CODE_QUERY_URI

__all__ = [
    "CityQueryApiClass"
]


class CityQueryApiClass(ApiBaseClass):

    uri = ORDER_CITY_CODE_QUERY_URI

    def __init__(self, model=None):
        super(CityQueryApiClass, self).__init__()
        self._model = model
