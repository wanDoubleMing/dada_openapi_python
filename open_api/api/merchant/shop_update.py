# -*- encoding: utf8 -*-
__author__ = 'wan'

from open_api.api.base import ApiBaseClass
from open_api.api.urls import MERCHANT_UPDATE_SHOP_URI


class ShopUpdateApiClass(ApiBaseClass):

    uri = MERCHANT_UPDATE_SHOP_URI

    def __init__(self, model=None):
        super(ShopUpdateApiClass, self).__init__()
        self._model = model
