"""
多个返回值
"""

# 演示多个变量接收多个返回值
def test_return():
  return 1,2

a,b = test_return()
print(a,b)