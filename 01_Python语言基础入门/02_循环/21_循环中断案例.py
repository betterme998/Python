'''
某公司，账户余额1w元，给20名员工发工资.
.1-20，依次每人可领取1000元
.领工资时，财务判断员工的绩效分1-10（随机），如果低于5，不发工资，下一位
.发完就结束
'''
import random
sum = 10000

for i in range(1,21):
    if sum <= 0:
        print("账户余额不足，无法发放工资")
        break
    num = random.randint(1, 10)
    if num < 5:
        print("第%d名员工绩效分%d不够，不发工资" % (i+1,num))
        continue
    else:
        sum -= 1000
        print("第%d名员工绩效分足够，发工资1000元，账户剩余%d" % (i+1, sum))