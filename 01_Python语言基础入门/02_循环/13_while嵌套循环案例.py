# 打印九九乘法表
x = 1

while x <= 9:
  y = 1
  while y <=x:
    print(f'{x}*{y}={x*y}\t',end=' ') #\t表示制表符 对齐方式
    y += 1
  print()
  x += 1
