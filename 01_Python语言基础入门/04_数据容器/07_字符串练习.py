"""
分隔字符串
给定一个字符串:"itheima itcast boxuegu"
统计字符串内有多少个"it"字符
将字符串内的空格，全部替换为字符:"|"
并按照"|"进行字符串分割，得到列表
"""
str = "itheima itcast boxuegu"
count = str.count("it")
print(f"it字符出现:{count}次")

new_str = str.replace(" ","|")
print(f"替换后的字符串:{new_str}")

new_str_list = new_str.split("|")
print(f"分割后的列表:{new_str_list}")