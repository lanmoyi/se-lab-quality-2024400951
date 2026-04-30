# after.py —— 重构完成，无坏味道 + 无敏感信息误报
def print_separator():
    print("========================")

def print_info(title, data):
    print_separator()
    print(title)
    for key, value in data.items():
        print(f"{key}：{value}")
    print_separator()

def print_circle_info(radius):
    area = 3.14 * radius * radius
    print_info("圆形信息", {
        "半径": radius,
        "面积": area
    })

def print_rectangle_info(length, width):
    area = length * width
    print_info("矩形信息", {
        "长": length,
        "宽": width,
        "面积": area
    })

def print_triangle_info(base, height):
    area = base * height / 2
    print_info("三角形信息", {
        "底": base,
        "高": height,
        "面积": area
    })

print_circle_info(5)
print_rectangle_info(4, 6)
print_triangle_info(3, 8)
