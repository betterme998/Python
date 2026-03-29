"""
演示对文件的读取
读操作相关方法  
read()方法:  
文件对象.read(num)  
num表示要从文件中读取的数据的长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据

readlines()方法:   
readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个
"""

# 打开文件夹
f = open("./index.txt", "r", encoding="utf-8")
print(type(f)) #<class '_io.TextIOWrapper'>对文本文档操作的类

# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}") # 3. 1415926
# print(f"读取全部字节的结果：{f.read()}") # 535 897932384626433832795028899375105.....国学Python来黑马，月薪过万。
# read多次读取会接着上一次读取的位置继续读取
print("-------------------------------------")

# 读取文件 - readlines() # 读取文件的全部行，封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}") # lines对象的类型：<class 'list'>
# print(f"lines的结果是：{lines}") # [] 空，因为文件指针已经到了文件末尾（读取文件指针会随着读取的内容移动，下一次读取接着指针位置读取）

# 读取文件 - readlind() # 一次性读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")# 第一行数据是：3. 1415926535
# print(f"第一行数据是：{line2}")# 第一行数据是：8979323846
# print(f"第一行数据是：{line3}")# 第一行数据是：2643383279

# for循环读取文件行
# for line in f:
#   print(f"每一行数据：{line}")

# 关闭文件
# f.close()

# with open 语法操作文件
with open("./index.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(f"每一行数据是: {line}")