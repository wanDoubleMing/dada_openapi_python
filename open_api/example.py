# -*- encoding: utf8 -*-
__author__ = 'wan'

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from open_api.dada_client import DadaApiClient
from open_api.dada_config import QAConfig, OnlineConfig
from open_api.api.merchant.shop_add import ShopAddApiClass
from open_api.api.merchant.shop_update import ShopUpdateApiClass
from open_api.api.merchant.merchant_add import MerchantAddApiClass
from open_api.model.merchant.shop_add import ShopAddModel
from open_api.model.merchant.shop_update import ShopUpdateModel
from open_api.model.merchant.merchant_add import MerchantAddModel
from open_api.api.order.order import OrderAddClass
from open_api.model.order.order import OrderModel


def shop_add_example():
    """
    添加门店的示例
    :return:
    """
    # 1.初始化客户端
    dada_client = DadaApiClient(QAConfig)

    # 2.选择一个api类,同时初始化api参数model
    shop_model = ShopAddModel()

    # 根据实际信息来填写
    shop_model.area_name = "xxxxxxxxxxx"
    shop_model.business = 1
    shop_model.city_name = "xxxxxxx"
    shop_model.contact_name = "xxxxxxx"
    shop_model.lat = 0
    shop_model.lng = 0
    shop_model.phone = "xxxxxxxxxxxxx"
    shop_model.station_address = "xxxxxxxxxxxxxxxx"
    shop_model.station_name = "测试sdk"
    shop_add_api = ShopAddApiClass(model=shop_model)

    # 3.rpc请求
    result = dada_client.do_rpc(api=shop_add_api)
    print result.to_string()


def add_order_example():
    """
    添加订单示例
    :return:
    """
    # 1.初始化客户端
    dada_client = DadaApiClient(QAConfig)

    # 2.选择一个api类,同时初始化api参数model
    order_model = OrderModel()

    # 填写门店编号
    order_model.shop_no = "xxxxxxxxxxxxx"

    # 填写订单编号
    order_model.origin_id = "xxxxxxxxxxxxxxx"
    order_model.cargo_price = 11
    order_model.city_code = "xxxxxxxxxxxxxx"
    order_model.is_prepay = 0
    order_model.receiver_name = "xxxxxxxxxxxxxx"
    order_model.receiver_address = "xxxxxxxxxxxxxx"
    order_model.receiver_lat = 0
    order_model.receiver_lng = 0
    order_model.receiver_phone = "xxxxxxxxxxxxx"

    # 填写回调URL, 每次订单状态变更就会通知该url(参见回调接口)
    order_model.callback = ""

    order_add_api = OrderAddClass(model=order_model)
    # 3.rpc请求
    result = dada_client.do_rpc(api=order_add_api)
    print result.to_string()


def merchant_add_example():
    """
    注册商户示例
    :return:
    """
    # 1.初始化客户端,注册商户的时候不需要source_id
    dada_client = DadaApiClient(QAConfig, is_user_source_id=False)

    # 2.选择一个api类,同时初始化api参数model
    merchant_add = MerchantAddModel()
    merchant_add.city_name = "xxxxxxxxxxx"
    merchant_add.enterprise_address = "xxxxxxxxxxxxxxxxx"
    merchant_add.enterprise_name = "xxxxxxxxxxxxxxx"
    merchant_add.contact_name = "xxxxxxxxxxxxxx"
    merchant_add.contact_phone = "xxxxxxxxxxxx"
    merchant_add.mobile = "xxxxxxxxxxxxxxx"
    merchant_add.email = "xxxxxxxxxxxxxxx"

    merchant_add_api = MerchantAddApiClass(model=merchant_add)
    # 3.rpc请求
    result = dada_client.do_rpc(api=merchant_add_api)
    print result.to_string()


def shop_update_example():
    """
    门店更新
    :return:
    """
    # 1.初始化客户端,注册商户的时候不需要source_id
    dada_client = DadaApiClient(OnlineConfig)

    # 2.选择一个api类,同时初始化api参数model
    shop_update_model = ShopUpdateModel()
    shop_update_model.origin_shop_id = "xxxxxxxxx"
    shop_update_model.city_name = "xxxxxxxxxx"
    shop_update_model.area_name = "xxxxxxxxxxxx"

    shop_update_api = ShopUpdateApiClass(model=shop_update_model)
    # 3.rpc请求
    result = dada_client.do_rpc(api=shop_update_api)
    print result.to_string()


if __name__ == '__main__':
    shop_update_example()
