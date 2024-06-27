"""
演示：list列表的常用操作
"""
# 查询list下标---------------------------------------------------------
mylist = [1, 2, 3]
# 1.1 查询某元素在列表中的位置
index = mylist.index(2)
print(f"2在列表中的位置是：{index}") # 1

# 1.2 查询的元素不在列表中
# index = mylist.index(4)
# print(f"2在列表中的位置是：{index}") # 报错ValueError: 4 is not in list

# 修改list---------------------------------------------------------------
# 2.1 修改列表中特定下标的元素
mylist[0] = 10
print(mylist) # [10, 2, 3]

# 插入元素---------------------------------------------------------------
# 3 在指定下标位置插入新元素
mylist.insert(0, 4)
print(mylist) # [4, 10, 2, 3]

# 追加元素---------------------------------------------------------------
# 4 在列表末尾追加元素
mylist.append(5)
print(mylist) # [4, 10, 2, 3, 5]
# 4.2追加元素2
mylist.extend([6, 7])
print(mylist) # [4, 10, 2, 3, 5, 6, 7]

# 删除元素---------------------------------------------------------------
element =  mylist.pop()# 删除列表末尾元素,并返回删除的元素
print(mylist) # [4, 10, 2, 3, 5 , 6]
print(element) # 6

# 删除指定下标元素
del mylist[0]
print(mylist) # [10, 2, 3, 5 , 6]

# 删除某元素在列表中第一个匹配项
mylist.remove(10)
print(mylist) # [2, 3, 5 , 6]

# 清空列表
mylist.clear()
print(mylist) # []

# 统计某个元素出现的次数--------------------------------------
mylist = [1, 2, 3, 4, 5, 6, 1]
count = mylist.count(1)
print(count) # 2

# 统计列表全部元素数量
count = len(mylist)
print(count) # 7
