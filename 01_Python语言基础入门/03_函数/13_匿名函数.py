"""
掌握lambda匿名函数语法
.lambda关键字，可以定义匿名函数（无名称）
"""
# 匿名函数语法：lambda 参数列表:返回值
def test_func(compute):
  print(compute(1, 2))

# 调用test_func函数，传入lambda匿名函数
test_func(lambda x, y: x + y)