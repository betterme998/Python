"""
(字符串相关工具，内含:)
--函数:str_reverse(s)，接受传入字符串，将字符串反转返回
--函数:substr(s，x，y)，按照下标x和y，对字符串进行切片
"""
def str_reverse(s):
    print(s[::-1])


def substr(s, x, y):
    print(s[x:y])