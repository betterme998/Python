"""
函数作为参数
"""

def tes_func(compute):
    result = compute(10, 2)
    print(result)
def compute(x, y):
    return x + y
tes_func(compute)
