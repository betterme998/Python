"""
演示面向对象类中的成员方法定义和使用
self关键字  
self关键字是成员方法定义的时候，必须填写的。  
它用来表示类对象自身的意思  
当我们使用类对象调用方法的是，self会自动被python传入  
在方法内部，想要访问类的成员变量，必须使用self

"""

# 定义一个带有成员方法的类
class Student:
  name = None #学生姓名

  def say_hi(self): # 必须有self参数
    print(f"大家好啊，我是{self.name}，欢迎大家多多关照")

  def say_hi2(self, msg):
    print(f"大家好，我是：{self.name}, {msg}")

stu = Student()
stu.name = "周杰伦"
stu.say_hi() # 大家好啊，我是周杰伦，欢迎大家多多关照
# 当我们使用类对象调用方法的是，self会自动被python传入  
stu.say_hi2("哎呦不错呦")

stu2 = Student()
stu2.name ="林俊杰"
stu2.say_hi() # 大家好啊，我是林俊杰，欢迎大家多多关照
stu2.say_hi2("小伙子我看好你")