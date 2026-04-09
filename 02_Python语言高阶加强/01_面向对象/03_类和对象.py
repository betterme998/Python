"""
1.掌握使用类描述现实世界事物的思想
.属性
.行为

2.掌握类和对象的关系
.类是程序中的“设计图纸”
.对象是基于图纸生产的具体实体

3.理解什么是面向对象
面向对象编程就是，使用对象进行编程
即，设计类，基于类创建对象，并使用对象来完成具体的工作


演示类和对象的关系，即面向对象的编程套路(思想)
"""

# 设计一个闹钟类
class Clock:
  id = None #序列化
  price = None #价格

  def ring(self):
    import winsound
    winsound.Beep(2000, 3000)


# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id}, 价格：{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID：{clock1.id}, 价格：{clock1.price}")
clock2.ring()