# 方式1：使用print直接输出类型信息
print(type("hello"))
print(type(123))
print(type(11.356))
# 方式2：使用变量存储type函数语句的结果
tring_type = type("hello")
int_type = type(123)
float_type = type(12.345)
print(tring_type)
print(int_type)
print(float_type)
# 方式3：使用type函数，查看变量中存储的数据类型信息
name = 123
print(type(name))