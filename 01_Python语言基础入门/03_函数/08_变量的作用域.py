"""
演示在函数使用的时候，定义变量作用域
"""

# 演示局部变量
# def test_a():
#   num = 100
#   print(num)
# test_a()
# print(num) # 报错

# 演示全局变量
# num = 100
# def test_a():
#   print(f"test_a :{num}") # 100

# def test_b():
#   print(f"test_b :{num}") # 100

# test_a()
# test_b()
# print(f"全局变量 :{num}") #100

# 在函数内修改全局变量
# num = 200

# def test_a():
#   print(f"test_a :{num}")

# def test_b():
#   num = 300
#   print(f"test_b :{num}")

# test_a()# 200
# test_b()# 300
# print(f"全局变量 :{num}") # 200

# global关键字，在函数内声明为全局变量
num = 200

def test_a():
  print(f"test_a :{num}")

def test_b():
  global num # 声明为全局变量
  num = 300
  print(f"test_b :{num}") 

test_a()# 200
test_b()# 300
print(f"全局变量 :{num}") # 300