# -*- encoding: utf8 -*-
__author__ = 'wan'

from open_api.api.urls import MERCHANT_REGISTER_URI
from open_api.api.base import ApiBaseClass


class MerchantAddApiClass(ApiBaseClass):

    uri = MERCHANT_REGISTER_URI

    def __init__(self, model=None):
        super(MerchantAddApiClass, self).__init__()
        self._model = model