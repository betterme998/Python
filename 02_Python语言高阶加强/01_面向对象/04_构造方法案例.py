"""
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的:
姓名、年龄、地址，这3类信息
请实现:
.通过for循环，配合input输入语句，并使用构造方法完成学生信息的键盘录入
.输入完成后，使用print语句，完成信息的输出

当前录入第1位学生信息，总共需录入10位学生信息
请输入学生姓名:周杰轮
请输入学生年龄:31
请输入学生地址:北京
学生1信息录入完成，信息为:【学生姓名:周杰轮，年龄:31，地址:北京】
当前录入第2位学生信息，总共需录入10位学生信息
请输入学生姓名：
"""

class EnterStudentInfo:
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address

  def print_info(self,num):
    print(f"学生{num}信息录入完成，信息为:【学生姓名:{self.name}，年龄:{self.age}，地址:{self.address}】")

for i in range(1,11):
  print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
  name = input("请输入学生姓名:")
  age = input("请输入学生年龄:")
  address = input("请输入学生地址:")
  EnterStudentInfo(name,age,address).print_info(i)
