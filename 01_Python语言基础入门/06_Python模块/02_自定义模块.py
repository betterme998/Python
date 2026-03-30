"""
Python中已经帮我们实现了很多的模块，
不过有时候我们需要一些个性化的模块，
这里就可以通过自定义模块实现，也就是自己制作一个模块
演示自定义模块

"""
# 导入自定义模块使用
# import my_module
# from my_module import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_module import test
# from my_module2 import test 
# test(1, 2) #会调用my_module2中的test


#__main__变
# 导入模块时，模块会被执行
# from my_module import test


#__all__变量
from my_module import *
test(1,2)
test_b(2,1) # 因为模版中有__all__ 变量，并且不包含test_b，所以报错