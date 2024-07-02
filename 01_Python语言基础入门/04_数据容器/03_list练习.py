# 数到 20 使⽤⼀个 for 循环打印数 1〜20（含）。
for i in range(1, 21):
    print(i) # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

#100 万 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个for 循环将这些数打印出来。（如果输出的时间太⻓，按 Ctrl + C 停⽌输出，或关闭输出窗⼝。）
# list_100w = list(range(1, 1000001))
# print(list_100w,end=',')

"""
100 万求和 创建⼀个包含数 1〜1 000 000 的列表，再使⽤
min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需
要多⻓时间。
"""
# list_100w = list(range(1, 1000001))
# print(min(list_100w),max(list_100w)) # 1,1000000
# print(sum(list_100w)) # 500000500000

"""
奇数 通过给 range() 函数指定第三个参数来创建⼀个列
表，其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出
来
"""
for i in range(1, 21, 2):
    print(i) # 1,3,5,7,9,11,13,15,17,19

"""
3 的倍数 创建⼀个列表，其中包含 3〜30 内能被 3 整除的
数，再使⽤⼀个 for 循环将这个列表中的数打印出来。
"""
for i in list(range(3, 31, 3)):
    print(i) # 3,6,9,12,15,18,21,24,27,30

"""
⽴⽅ 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2
的⽴⽅⽤ 2**3 表⽰。创建⼀个列表，其中包含前 10 个整数（1〜
10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。
"""
list_10 = [value**3 for value in range(1, 11)]
for i in list_10:
    print(i) # 1,8,27,64,125,216,343,512,729,1000


"""
删除为特定值的所有列表元素
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')
print(pets)

"""
一个列表内容：[21,25,21,23,22,20]
1.定义这个列表，使用变量接受它
2.追加一个数字31，到列表尾部
3.追加一个新列表[29,33,30]到尾部
4.取出第一个元素（21）
5.取出最后一个元素（30）
6.查找元素31，在列表下标位置
"""
age = [21,25,21,23,22,20]
age.append(31)
print(age)
age.extend([29,33,30])
print(age)
end_age = age.pop()
print(end_age)
print(age)
one_age = age.pop(0)
print(one_age)
print(age)  
index = age.index(31)
print(index)


"""
取出列表中的偶数[1,2,3,4,5,6,7,8,9,10]
.取出偶数并存入新列表对象中
.使用while循环和for循环各操作一次
"""
list_num = [1,2,3,4,5,6,7,8,9,10]
list_num2 = []
list_num3 = []
index = 0
while index < len(list_num):
   if list_num[index] % 2 == 0:
       list_num2.append(list_num[index])
   index += 1
print(list_num2)

for item in list_num:
   if item % 2 == 0:
       list_num3.append(item)
print(list_num3)



