# -*- encoding: utf8 -*-
__author__ = 'wan'

from open_api.model.base import BaseModel


class ShopUpdateModel(BaseModel):

    def __init__(self):
        """
        新增门店接口
        :return:
        """
        self.origin_shop_id = None
        self.city_name = None
        self.area_name = None

    def field_check(self):
        """
        校验必填参数
        :return:
        """
        if self.origin_shop_id is None:
            raise TypeError("%s value can not be null" % "origin_shop_id")

        return True