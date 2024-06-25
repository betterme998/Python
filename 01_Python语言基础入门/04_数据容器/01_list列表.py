"""
演示数据容器之：list列表
"""

# 定义一个列表
list1 = [1, 2, 3]
print(list1)
print(type(list1))

my_list = [1, 2, "hello", [1, 2], (3, 4)]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
list2 = [1, 2, ["a", "b"], (3, 4)]
print(list2)
print(type(list2))

# 通过下标索引取出对应位置的数据
my_list = [1, 2, "hello", [1, 2], (3, 4)]
print(my_list[0])# 取出第一个元素
print(my_list[-1])# 取出最后一个元素

# 取出嵌套列表中的元素
my_list = [1, 2, ["a", "b"], (3, 4)]
print(my_list[2][1])# 取出嵌套列表中的第二个元素