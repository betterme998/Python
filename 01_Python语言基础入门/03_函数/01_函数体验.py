# 需求：统计字符串的长度，不使用内置函数len()

str1 = 'hello'
str2 = 'world'
str3 = 'python'

# 定义一个函数
def my_len(data):
    # 函数的说明文档
    """
    函数说明
    :param data: 参数
    :return: 返回值
    """
    count = 0
    for i in data:
        count += 1
    print(count)

my_len(str1)
my_len(str2)
my_len(str3)
