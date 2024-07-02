"""
演示对序列进行切片操作
"""

# 1. 列表切片操作，从1开始，4结束，步长1
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[1:4])# [2,3,4]

# 对tuple切片操作，从头开始，到最后，步长1
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[:])# (2,3,4,5)

# 对str进行切片操作，从头开始，到最后，步长2
my_str = "hello world"
print(my_str[::2])# hlowrd

# 对str进行切片操作，从头开始，到最后，步长-1
my_str = "hello world"
print(my_str[::-1])# dlrow olleh

# 对列表进行切片，从3开始，到1结束，步长-1 
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[3:1:-1])# [4, 3]

# 对元组进行切片，从头开始，到尾结束，步长-2
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[::-2])