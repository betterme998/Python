"""
演示异常的传递性

"""
# 定义一个出现异常的方法
def fun1():
  print("fun1 开始执行")
  num = 1/0#肯定有异常，除以0的异常
  print("func1 结束执行")

# 定义一个无异常的方法。调用上面的方法
def fun2():
    print("fun2 开始执行")
    fun1()
    print("func2 结束执行")

# 定义一个方法、调用上面的方法
def main():
  try:
     fun2()
  except Exception as e:
     print("main 方法捕获异常：",e)
main()