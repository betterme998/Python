"""
猜1-100随机数
"""
import random
num = random.randint(1, 100)
i = 1
print(num)
input_num = int(input("您猜的1-100的随机数字是："))
while input_num != num:
    i+=1
    if input_num > num:
        print("您猜的数字大了")
        input_num = int(input("您猜的1-100的随机数字是："))
    else:
        print("您猜的数字小了")
        input_num = int(input("您猜的1-100的随机数字是："))
print("恭喜您猜对了，一共猜了%d次" % i)
    