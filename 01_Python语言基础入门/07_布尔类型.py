# 比较运算符的应用 - 演示布尔类型的定义

#定 义变量存储布尔类型的数据

bool_1 = True
bool_2 = False
print("bool_1:", bool_1,"类型是：",type(bool_1))

# 比较运算符的使用
# ==, !=, >, <, >=, <=

# 演示进行内容相等比较
num1 = 10
num2 = 10
print(f"10 == 10的结果是：",{num1 == num2})
num1 = 10
num2 = 15
print(f"10 != 15的结果是：",{num1 != num2})

# 演示进行内容大小比较
num1 = 20
num2 = 10
print(f"20 > 10的结果是：",{num1 > num2})

num1 = 20
num2 = 10
print(f"20 < 10的结果是：",{num1 < num2})
