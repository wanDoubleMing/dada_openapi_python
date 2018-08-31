# -*- encoding: utf8 -*-
__author__ = 'wan'

from open_api.api.base import ApiBaseClass
from open_api.api.urls import MERCHANT_ADD_SHOP_URI
import json

class ShopAddApiClass(ApiBaseClass):

    uri = MERCHANT_ADD_SHOP_URI

    def __init__(self, model=None):
        super(ShopAddApiClass, self).__init__()
        self._model = model

    def get_business_params(self):
        """
        shopadd是一个批量添加的接口
        :return:
        """
        single_data = self._model.to_dict()
        return json.dumps([single_data])