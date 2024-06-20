print(666)
print(666)
print("hahah")

# 字符串多种定义方式
# 1. 单引号
name = 'zhangsan'
print(name)

# 2. 双引号
name = "zhangsan"
print(name)

# 3. 三引号 支持多行写法
name = '''zhangsan
haha
'''
print(name)

# 字符串内包含双引号
name = '"zhangsan"'

# 字符串内包含单引号
name = "'zhangsan'"

#使用转义字符 \ 解除引号的效果
name = '\"zhangsan\"'
print(name)


# 字符串拼接
print("zhangsan" + "123")

# 字符串字面量和字符串变量拼接
name = "zhangsan"
address = "beijing"
print(name + address)

# 字符串格式化输出
# 数字被转换成字符串拼接进去
class_num = 57
avg_salary = 16781
message = "Python大数据北京%s班，平均薪资%s元" % (class_num, avg_salary)
print(message)

name = "hahah"
year = 2019
price = 10.5
message = "%s今年%d岁，买了%f元" % (name, year, price)
print(message)

# 字符串的精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

# 字符串格式化方式 2
# 不关心类型，不做精度控制
name = "zhangsan"
year = 2019
price = 10.5
print(f"名字是{name}，今年{year}岁，买了{price}元")

#对表达式进行格式化 
# .表达式：一条具有运算结果的语句，如 1+2
print("1*1 的结果是: %d" % (1*1)) # 1\*1 的结果是: 1
print("字符串在 python 中的类型是: %s" % type("字符串"))


