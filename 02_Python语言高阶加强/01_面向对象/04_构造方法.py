"""
1.掌握使用构造方法向成员变量赋值


# 演示类的构造方法

1.构造方法的名称是:__init__注意init前后的2个下划线符号

2.构造方法的作用:
.构建类对象的时候会自动运行
.构建类对象的传参会传递给构造方法，借此特性可以给成员变量赋

3.注意事项:
构造方法不要忘记self关键字
在方法内使用成员变量需要使用self

"""

# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__

class Student:
  def __init__(self, name, age, tel): # 构造方法会自动执行，要传入self
    self.name = name
    self.age = age
    self.tel = tel
    print("Student类构建了一个类对象")

stu = Student("周杰伦", 18, "12345678912")
print(stu.name)
print(stu.age)
print(stu.tel)

"""
Student类构建了一个类对象
周杰伦
18
12345678912
"""
