# DadaOpenApi
Demo of Dada openapi for different development languages (java, php, python)
</br>
达达开放平台的接口示例（python版）
</br>

## 使用说明（可以参照example.py文件）
</br>
### 1.初始化配置文件
</br>
填充app_key,app_secret文件等。
</br>
```
APP_KEY = ""
APP_SECRET = ""
HOST = ""
SOURCE_ID = ""
```
</br>

### 2.初始化客户端
</br>
```
dada_client = DadaApiClient(QAConfig) # 根据环境选择合适的配置对象
```
</br>

### 3.初始化数据模型类
</br>
注意：新建一个模型的时候，必须实现```field_check()```方法，用来作必填参数的校验。
</br>
```
# 新增订单模型
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
```
</br>

### 4.初始化接口类
</br>
```
order_add_api = OrderAddClass(model=order_model)
```
</br>

### 5.rpc请求
</br>
```
result = dada_client.do_rpc(api=order_add_api)
print result.to_string()
```
</br>
以上为一个完整的请求
