# if语句的基本格式应用

age = 30

if age >= 18:
    print("成年人")

if age >=114:
    print("已经过世了")

if not age >= 18:  # not表示非,反过来
    print("未成年人")



# if...elif语句应用
age = int(input("请输入你的年龄："))

if age >= 18:
    print("成年人")
else:
    print("儿童")


# if...elif...else语句应用
height = int(input("请输入你的身高："))
vip = int(input("请输入你的VIP等级："))

# 第一个条件
if height < 120:
    print("身高小于120，能参加活动")
elif vip > 3:
    print("VIP等级大于3，可以参加活动")
else:
    print("不能参加活动")

# 优化
if int(input("请输入你的身高：")) < 120:
    print("身高小于120，能参加活动")
elif int(input("请输入你的VIP等级：")) > 3:
    print("VIP等级大于3，可以参加活动")
else:
    print("不能参加活动") 

# 判断语句嵌套
print("欢迎来到动物园")
if int(input("请输入你的身高：")) > 120:
    print("身高大于120，不能参加活动")
    print("请选择其他活动")
    if int(input("请输入你的VIP等级：")) > 3:
        print("VIP等级大于3，可以参加活动")
    else:
        print("不能参加活动")
else:
    print("身高小于120，能参加活动")

# 1.检查多个条件
age1 = 20
age2 = 18
age1 >= 20 and age2 >= 20 # 两个条件同时成立，结果才为真
age1 >= 20 or age2 >= 20 # 两个条件有一个成立，结果就为真

# 2.检查特定值是否在列表中
num = [1, 2, 3]
1 in num # 结果为真
4 not in num # 结果为真