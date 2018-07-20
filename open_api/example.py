# -*- encoding: utf8 -*-
__author__ = 'wan'

from open_api.dada_client import DadaApiClient
from open_api.dada_config import QAConfig
from open_api.api.order import OrderAddClass
from open_api.api.city_code import CityQueryApiClass


def example():
    # 1.初始化客户端
    dada_client = DadaApiClient(QAConfig)

    # 2.选择一个api类,同时初始化api参数model
    city_api = CityQueryApiClass()

    # 3.rpc请求
    result = dada_client.do_rpc(api=city_api)
    print result.to_string()


if __name__ == '__main__':
    example()
