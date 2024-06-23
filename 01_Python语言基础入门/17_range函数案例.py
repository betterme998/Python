'''
定义一个数字变量num，，内容随意
并使用range()语句获取1到num的序列，使用for循环遍历它
在遍历的过程中，统计有多少个偶数出现
'''

num = 100
count = 0
for a in range(1,num+1):
  print(a)
  if a%2==0:
    print("偶数")
    count += 1
print(f"有{count}个偶数")