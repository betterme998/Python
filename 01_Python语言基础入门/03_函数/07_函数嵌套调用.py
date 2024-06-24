'''
演示嵌套调用函数
'''

# 定义函数func_b
def func_b():
    print('func_b')

# 定义函数func_c
def func_c():
    print('func_c')
    func_b()

# 调用函数func_c
func_c()