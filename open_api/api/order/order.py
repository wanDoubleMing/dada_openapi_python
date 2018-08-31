# -*- encoding: utf8 -*-

from open_api.api.base import ApiBaseClass
from open_api.api.urls import ORDER_ADD_URI


__all__ = [
    "OrderAddClass"
]


class OrderAddClass(ApiBaseClass):

    uri = ORDER_ADD_URI

    def __init__(self, model=None):
        """
        :return:
        """
        super(OrderAddClass, self).__init__()
        self._model = model





