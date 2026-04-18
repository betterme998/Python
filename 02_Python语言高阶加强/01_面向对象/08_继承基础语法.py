"""
演示面向对象：继承的基础语法
"""

# 演示单继承
class Phone:
  IMEI = None # 序列号
  producer = None # 厂商

  def call_by_4g(self):
    print("4g通话")

class Phone2(Phone):
  face_id = "10001"  # 面部识别ID

  def call_by_5g(self):
    print("5g通话")

phone = Phone2()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承

class NFCReader:
  nfc_type = "第五代"
  producer = "HM"

  def read_card(self):
    print("NFC读卡")

  def write_card(self):
    print("NFC写卡")

class RemoteControl:
  rc_type = "红外遥控"

  def control(self):
    print("红外遥控开启了")

# 左边优先
class MyPhone(Phone, NFCReader, RemoteControl):
  pass # 空语句，表示什么都不做

phone = MyPhone()
phone.call_by_4g()

phone.read_card()
phone.control()# 演示多继承下，父类成员名一致的场景