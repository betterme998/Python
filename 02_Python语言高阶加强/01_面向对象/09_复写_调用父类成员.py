"""
1.掌握复写父类成员的语法
2.掌握如何在子类中调用父类成员
"""

class Phone:
  IMEI = None #序列号
  producer = "ITCAST" # 厂商

  def call_by_5g(self):
    print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
  producer = "ITHEIMA" #复写父类的成员属性

  def call_by_5g(self):
    print("开启CPU单核模式，确保通话时省电")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 在子类中，调用父类成员