'''
for循环打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (j, i, i * j), end=' ')
    print()

'''

for i in range(1,10):
  for j in range(1,i+1):
    print(f'{j}*{i} = {j*i}\t', end= ' ')
  print()
