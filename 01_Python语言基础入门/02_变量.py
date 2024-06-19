"""
演绎python中变量
"""

# 定义一个变量，用来记录钱包余额
money = 100

#通过print语句，打印出钱包余额
print("钱包还有：", money)

# 买了一个冰淇淋，花费10元
money -= 10
print("钱包还有：", money)

# 每隔一小时，输出一下钱包余额
print("现在是下午1点，钱包还有：", money)
print("现在是下午2点，钱包还有：", money)
print("现在是下午3点，钱包还有：", money)
print("现在是下午4点，钱包还有：", money)
