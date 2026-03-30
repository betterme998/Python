"""
主动写一段错误代码，演示异常的出现
"""

# 通过open，读取一个不存在的文件
f = open("./index.txt","r",encoding="utf-8")
"""
Traceback (most recent call last):
  File "D:\代码\Python\01_Python语言基础入门\05_文件和异常\03_异常\01_了解异常.py", line 6, in <module>
    f = open("./index.txt","r",encoding="utf-8")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './index.txt'
"""