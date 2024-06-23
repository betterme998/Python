# 定义字符串变量，内容为"irheima is a brand of itcast",通过for循环，遍历此英文字母：“a”

name = "irheima is a brand of itcast"
sum = 0
for a in name:
    print(a)
    if a == "a":
       sum += 1
print(f"出现{sum}次a")