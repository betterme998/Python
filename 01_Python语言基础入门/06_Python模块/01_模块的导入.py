"""
什么是模块  
Python 模块(Module)，是一个 Python 文件，以.py 结尾. 模块能定义函数，类和变量，模块里也能包含可执行的代码

大白话:模块就是一个Python文件，里面有类、函数、变量等，我们可以拿过来用(导入模块去使用)

模块的导入方式
模块在使用前需要先导入 导入的语法如下
[from 模块名] import [模块 | 类|变量 | 函数 | *][as 别名]
常用的组合形式如:
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import*
import 模块名 as 别名
from 模块名 import 功能名 as 别名

演示Python的模块导入

"""

# 使用import号入time模块使用sleep功能(函数)
# import time # 导入Python内置的time硬块(time.py这个代码文件)
# print("你好")
# time.sleep(5) #睡眠5秒
# print("再见")

# 使用from导入time的sleep功能(函数)
# from time import sleep
# print("你好")
# sleep(5) #睡眠5秒
# print("再见")

# 使用* 号入time摸块的全部功能
# from time import * # *表示全部的意思
# print("你好")
# sleep(5) #睡眠5秒
# print("再见")

# 使用as给特定功随加上别名
# import time as t 

from time import sleep as sl
print("你好")
sl(5) #睡眠5秒
print("再见")
