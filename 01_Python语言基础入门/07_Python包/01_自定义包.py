"""
什么是Python包  
从物理上看，包就是一个文件夹，在该文件夹下包含了一个 _init_.py 文件，该文件夹可用于包含多个模块文件  
从逻辑上看，包的本质依然是模块
演示Python的包

我们创建的包内一定包含一个__init__.py文件
里面也可以使用__all__变量, 来控制import *时，可以导入哪些模块

"""

# 创建一个包
# 导入自定义的包中的模块，并使用
# import my_package.my_module1
# import my_package.my_module2

# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2

# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import* 再包的_init_.py 文件中
from my_package import *
my_module1.info_print1()
my_module2.info_print2()