"""
演示面向对象封装思想中私有成员的使用
私有成员:不公开的属性和行为  
类中提供了私有成员的形式来支持.
.私有成员变量
.私有成员方法

定义私有成员的方式:  
.私有成员变量：变量名以__开头（2个下划线）
.私有成员方法：方法名以__开头（2个下划线）
"""

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
  # 私有的成员变量
  __current_voltage = 1 # 当前手机运行电压
 # 私有的成员方法
  def __keep_single_core(self):
    print("让CPU以单核模式运行")

  #内部方法可以访问私有成员变量，私有成员方法
  def call_by_5g(self):
    if self.__current_voltage >= 1:
      print("5g通话已开启")
    else:
      self.__keep_single_core()
      print("电量不足，无法使用5g通话，并已设置为单核运行进行省电模式")

phone = Phone()

# 私有成员无法被类对象使用，但是可以被其它的成员使用
# print(phone.__current_voltage) # Phone' object has no attribute '__current_voltage'
# phone.__keep_single_core() #'Phone' object has no attribute '__keep_single_core'.

phone.call_by_5g()