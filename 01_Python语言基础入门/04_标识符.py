# 规则1：内容限定，限定只能使用：中文，英文，数字，下划线，注：不能以数字开头
# 错误的代码示范： 1_name = 123
# 错误的代码示范：name_! = 123
name_ = "张三"
_name = 123
name_ = "李四"

# 规则2：不能使用关键字，如：print, if, for, while, def, class, pass, return, break, continue
# 错误的代码示范： class = 123
# 错误的代码示范： if = 1
name = 123

# 规则3：大小写敏感，如：name, Name, NAME
Itheima = 123
itheima = "渐进"
print(Itheima)
print(itheima)