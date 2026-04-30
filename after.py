# after.py —— 重构完成，无坏味道
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

print_user_info("张三", 20, "男")
print_product_info(1001, "笔记本", 4999)
print_order_info(5001, "2025-01-01", "已支付")
