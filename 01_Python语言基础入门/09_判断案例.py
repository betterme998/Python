'''
1.数字随机产生，范围1-10
2.3次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了小了
'''
import random
num = random.randint(1, 10)
print("随机产生的数字是：", num)
count = int(input("请猜出1-10中出现的数字："))
if num == count:
  print("恭喜你，猜对了！") 
else:
  if num > count:
    print("猜小了") 
    count = int(input("第二次请猜出1-10中出现的数字："))
    if num == count:
      print("恭喜你，猜对了！") 
    else:
      if num > count:
        print("猜小了") 
        count = int(input("第三次请猜出1-10中出现的数字："))
        if num == count:
          print("恭喜你，猜对了！") 
        elif num > count:
          print("猜大了，结束") 
        else:
          print("猜小了，结束") 
  else:
    print("猜大了")
    count = int(input("第二次请猜出1-10中出现的数字："))
    if num == count:
      print("恭喜你，猜对了！") 
    else:
      if num > count:
        print("猜小了") 
        count = int(input("第三次请猜出1-10中出现的数字："))
        if num == count:
          print("恭喜你，猜对了！") 
        elif num > count:
          print("猜大了，结束") 
        else:
          print("猜小了，结束") 
