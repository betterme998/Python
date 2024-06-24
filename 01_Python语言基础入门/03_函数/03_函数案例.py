# 定义一个函数，名称任意，并接受一个参数传入（数字类型），在函数内进行体温判断（正常小于37.3）

def str_plus(num):
  if num < 37.3:
    print("正常")
  else:
    print("异常")

str_plus(38.3)