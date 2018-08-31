# -*- encoding: utf8 -*-
__author__ = 'wan'

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from open_api.dada_client import DadaApiClient
from open_api.dada_config import QAConfig
from open_api.api.merchant.shop_add import ShopAddApiClass
from open_api.api.merchant.merchant_add import MerchantAddApiClass
from open_api.model.merchant.shop_add import ShopAddModel
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
    shop_model.area_name = "浦东新区"
    shop_model.business = 1
    shop_model.city_name = "上海"
    shop_model.contact_name = "达达"
    shop_model.lat = 31.228623
    shop_model.lng = 121.587172
    shop_model.phone = "13809126789"
    shop_model.station_address = "隆宇大厦"
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
    order_model.shop_no = "11664071"
    order_model.origin_id = "test0000000001"
    order_model.cargo_price = 11
    order_model.city_code = "021"
    order_model.is_prepay = 0
    order_model.receiver_name = "测试达达"
    order_model.receiver_address = "虹口足球场"
    order_model.receiver_lat = 31.228623
    order_model.receiver_lng = 121.587172
    order_model.receiver_phone = "13798061234"
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
    merchant_add.city_name = "上海"
    merchant_add.enterprise_address = "上海隆宇大厦"
    merchant_add.enterprise_name = "测试上海sdk"
    merchant_add.contact_name = "测试达达"
    merchant_add.contact_phone = "13798061234"
    merchant_add.mobile = "13798061234"
    merchant_add.email = "13798061234@qq.com"

    merchant_add_api = MerchantAddApiClass(model=merchant_add)
    # 3.rpc请求
    result = dada_client.do_rpc(api=merchant_add_api)
    print result.to_string()



if __name__ == '__main__':
    merchant_add_example()
