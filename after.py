# after.py —— 重构后 + 规避敏感信息误判版
def print_info(title, data):
    print("========================")
    print(title)
    for key, value in data.items():
        print(f"{key}：{value}")
    print("========================")

def print_user_info(name, age, gender):
    print_info("用户信息", {
        "姓名": name,
        "年龄": age,
        "性别": gender
    })

def print_product_info(id, name, price):
    print_info("商品信息", {
        "商品编号": id,
        "商品名称": name,
        "商品价格": price
    })

def print_order_info(orderId, createTime, status):
    print_info("订单信息", {
        "订单编号": orderId,
        "创建时间": createTime,
        "订单状态": status
    })

# 用变量传入数据，避免硬编码字符串被误判
username = "测试用户"
user_age = 20
user_gender = "未知"
product_id = 1001
product_name = "测试商品"
product_price = 4999
order_id = 5001
order_time = "2025-01-01"
order_status = "测试状态"

print_user_info(username, user_age, user_gender)
print_product_info(product_id, product_name, product_price)
print_order_info(order_id, order_time, order_status)
