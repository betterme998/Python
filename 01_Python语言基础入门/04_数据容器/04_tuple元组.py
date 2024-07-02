"""
⾃助餐 有⼀家⾃助式餐馆，只提供 5 种简单的⾷品。请
想出 5 种简单的⾷品，并将其存储在⼀个元组中。
使⽤⼀个 for 循环将该餐馆提供的 5 种⾷品都打印出来。
尝试修改其中的⼀个元素，核实 Python 确实会拒绝你这样做。
餐馆调整菜单，替换了两种⾷品。请编写⼀⾏给元组变量赋值的
代码，并使⽤⼀个 for 循环将新元组的每个元素都打印出来
"""
foot = ("西红柿", "豆包", "油条", "炸鸡", "面包")
for i in foot:
    print(i)
# foot[1] = "豆芽" # 报错 元组不能修改里面的元素
foot = ("西红柿", "豆包", "油条", "豆腐卤", "烧汤粉")
for i in foot:
    print(i)


# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(type(t1))

# 定义单个元素的元组
# 当元组中只有单个元素，元素后面必须加上,号，不加就不是元组
t4 = (1,)
print(type(t4))

# 元组的嵌套
t5 = (1, "hello", True, [1, 2], (5,6))
print(type(t5))

#下标索引取出内容
print(t5[4][1])

# 元组的操作：index查找方法
t6 = ("a", "b", "c")
index = t6.index("c")
print(index)

#元组的操作：count统计方法
t7 = ("a", "b", "c", "a")
count = t7.count("a")
print(f"a出现了:{count}次")

# 元组的操作：len求长度
t8 = ("a", "b", "c")
print(len(t8))

# 元组的遍历：while
t9 = ("a", "b", "c")
index = 0
while index < len(t9):
    print(t9[index])
    index += 1

# 元组的遍历: for
for item in t9:
    print(item)

# 修改元组内容,我们没有直接改元组，而是改元组当中的list的值。正常运行
t10 = (1, 2, [4, 5])
print(f"t10内容是:{t10}")
t10[2][0] = 3
t10[2][1] = 4
print(f"t10内容是:{t10}")