"""
演示以数据容器的角色：学习字符串的相关操作
"""
my_str = 'hello world'
# 通过下标索取值
value = my_str[2]
value2 = my_str[-2]
print(value,value2)

# my_str[2] = "y" 报错，不能修改

# index方法
value =  my_str.index('o')
print(value)

# replace方法 替换字符串中指定的字符,返回一个新的字符串
new_my_str = my_str.replace('o','a')
print(new_my_str) 

# split方法 
# 按照指定的分隔符将字符串分割成多个子串，返回一个列表
# 字符串本身不变
my_str = "hello world 1"
my_str_list = my_str.split(" ")
print("my_str_list:", my_str_list) # ['hello', 'world', '1']

# strip方法
# 去除前后空格
my_str = " hello worle "
new_my_str = my_str.strip() #不传参数
print(new_my_str)

my_str = "12hello worle21"
new_my_str = my_str.strip("12") # 会按照1，2进行去除
print(new_my_str)

# count方法
# 统计字符串中字符出现的次数
my_str = "112211122"
print(my_str.count("1"))

# len方法
# 统计字符串的长度
my_str = "123456789"
print(len(my_str))