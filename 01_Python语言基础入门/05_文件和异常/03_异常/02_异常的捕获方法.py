"""
演示捕获异常
"""

# 基本捕获语法
# 捕获所有异常
try:
  f = open("./index.txt", "r", encoding="utf-8")
except:
  print("出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
  f = open("./index.txt", "w", encoding="utf-8")

#捕获指定异常
try:
  print(name)
except NameError as e:
  print("出现了变量未定义的异常")

#捕获多个异常
try:
  # 1/0
  print(name)
except (NameError,ZeroDivisionError) as e: #使用元组
  print("出现了变量未定义 或者 除以0的异常错误")

#未正确设胃捕获异常类型、将无法捕获异常


#描获所有异常
try:
  f = open("./index.txt","r",encoding="utf-8")
except Exception as e:
  print("出现异常了")
else:
  print("没有异常 ")
finally:
  print("无论是否捕获，都会执行")
  f.close()