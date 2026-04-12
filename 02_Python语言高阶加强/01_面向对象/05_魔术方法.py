"""
1. 掌握几种常用的类内置方法
演示Python内置的各类魔术方法
"""

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age  
  # __init__  魔术方法
  def __str__(self): #必须传self
    return f"Srudent类对象, name:{self.name}, age:{self.age}"
  
  # __lt__  魔术方法 小于、大于符号比较 (两个对象比较)
  def __lt__(self, other): # other 另一个类对象
    return self.age < other.age
  
  # __le__ 魔术方法 <=, >=两种比较运算符上
  def __le__(self, other): #必传self，other另一个类对象
    return self.age <= other.age
  
  # __eq__  魔术方法 等于符号比较
  # 不实现__eq__方法，比较内存地址，即比较是否同一个对象  
  # 实现__eq__方法，就可以按照自己的想法决定2个对象是否相同
  def __eq__(self, other):
    return self.age == other.age



  

# __str__  魔术方法 字符串方法  
stu = Student("周杰伦", 18)
print(stu) # Srudent类对象, name:周杰伦, age:18
print(str(stu)) # Srudent类对象, name:周杰伦, age:18
# 如果不写__str__ ，会打印内存地址<__main__.Student object at 0x000001773711A150>



# __lt__(self, other)  魔术方法 小于、大于符号比较 
"""
传入参数：other，另一个类对象
返回值：True / False
内容：自行定义
"""
stu2 = Student("林俊杰", 18)
print(stu < stu2) # True
print(stu > stu2) # False



# __le__  魔术方法 小于等于、大于等于符号比较
#传入参数：other，另一个类对象
#返回值：True / False
print(stu <= stu2)# True
print(stu >= stu2)# False



# __eq__  魔术方法 等于符号比较
print(stu == stu2) # true

