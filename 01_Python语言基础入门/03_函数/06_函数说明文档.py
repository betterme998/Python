# 函数说明文档

# 定义函数，进行文档说明
def add(x, y):
  """
  函数说明文档
  接受两个参数，进行相加
  :param x: 参数1是数字
  :param y: 参数2是数字
  :return: 返回值是两数相加的结果
  """
  result = x + y
  print(result)
  return result
add(1, 2)