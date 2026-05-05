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
    # 在子类中，调用父类成员（复写后调用父类）
    # 方式一
    # print(f'父类的厂商是：{Phone.producer}')
    # Phone.call_by_5g(self)

    #方式二
    print(f'父类的厂商是：{super().producer}') #super() 表示父类
    super().call_by_5g()

    print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

