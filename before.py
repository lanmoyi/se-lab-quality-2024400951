# before.py —— 包含典型代码坏味道
def print_user_info(name, age, gender):
    print("========================")
    print("姓名：" + name)
    print("年龄：" + str(age))
    print("性别：" + gender)
    print("========================")
    unused_variable = 100

def print_product_info(id, name, price):
    print("========================")
    print("商品编号：" + str(id))
    print("商品名称：" + name)
    print("商品价格：" + str(price))
    print("========================")
    unused_var2 = 200

def print_order_info(orderId, createTime, status):
    print("========================")
    print("订单编号：" + str(orderId))
    print("创建时间：" + createTime)
    print("订单状态：" + status)
    print("========================")
    unused_var3 = 300

print_user_info("张三", 20, "男")
print_product_info(1001, "笔记本", 4999)
print_order_info(5001, "2025-01-01", "已支付")
