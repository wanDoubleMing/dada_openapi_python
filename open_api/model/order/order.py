# -*- encoding: utf8 -*-
from open_api.model.base import BaseModel


class OrderModel(BaseModel):

    def __init__(self):
        """
        业务参数
        :return:
        """
        self.shop_no = None
        self.origin_id = None
        self.city_code = None
        self.cargo_price = None
        self.is_prepay = 0
        self.receiver_name = None
        self.receiver_address = None
        self.receiver_lat = None
        self.receiver_lng = None
        self.callback = None
        self.receiver_phone = None

    def field_check(self):
        """
        :return:
        """
        for key, value in self.__dict__.iteritems():
            if value is None:
                raise TypeError("%s value can not be null" % key)

        return True
