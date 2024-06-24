# 演示循环语句的中断控制：break和continue

# 循环中断语句 continue
# for i in range(1, 6):
#   print("语句1")
#   continue
#   print("语句2")

# continue的嵌套应用
# for i in range(1,6):
#   print("语句1")
#   for j in range(1,6):
#     print("语句2")
#     continue
#     print("语句3")
#   print("语句4")

# break的应用
# for i in range(1, 101):
#   print("语句1")
#   break
#   print("语句2")
# print("语句3")

# break的嵌套应用
for i in range(1, 6):
  print("语句1")
  for j in range(1, 6):
    print("语句2")
    break
    print("语句3")
  print("语句4")