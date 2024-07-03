"""
集合使用
"""

# 定义集合
my_set = {"a", "b", "c"}
my_set_empy = set()
print(f"my_set:{my_set},类型:{type(my_set)}")
print(f"my_set_empy:{my_set_empy},类型:{type(my_set_empy)}")

# 添加新元素
my_set.add("d")
print(f"my_set:{my_set}")

# 移除元素
my_set.remove("d")
print(f"my_set:{my_set}")

# 随机取出一个元素
my_set = {"a", "b", "c", "d"}
element = my_set.pop()
print(f"element:{element}")
print(f"my_set:{my_set}")

# 清空集合
my_set.clear()
print(f"my_set:{my_set}")

# 取2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set_diff = set1.difference(set2)
print(f"set_diff:{set_diff}")
print(f"set1:{set1}")
print(f"set2:{set2}")

# 消除两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2) # 直接修改set1,删除和set2相同的元素
print(f"set1:{set1}")
print(f"set2:{set2}")

# 2个集合合并一个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set_union = set1.union(set2)
print(f"set_union:{set_union}")
print(f"set1:{set1}")
print(f"set2:{set2}")

# 统计集合元素数量
set1 = {1, 2, 3}
print(len(set1))


# 集合的遍历