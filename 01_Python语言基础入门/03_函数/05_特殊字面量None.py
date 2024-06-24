def say_hi():
  print('hi')
result = say_hi()
print(f"无返回值的函数，返回的内容{result}") # None
print(f"无返回值的函数，返回的内容类型是{type(result)}") #<class 'NoneType'>

# 主动返回None的函数
def say_hi2():
  print('hi')
  return None
result = say_hi2()
print(f"无返回值的函数，返回的内容{result}") # None
print(f"无返回值的函数，返回的内容类型是{type(result)}") #<class 'NoneType'>

# None用于if判断
def check_age(age):
  if age < 18:
    return None
  else:
    return "SUCCESS"

result = check_age(17)
if not result:
  print("未成年")

# None 用于声明无初始值内容的变量
name = None