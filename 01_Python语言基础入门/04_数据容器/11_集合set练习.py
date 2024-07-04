"""
有如下列表对象:
my_list =[黑马程序员’，传智播客，黑马程序员’传智播客’itheima','itcast','itheima'，'itcast''best']
请定义一个空集合
通过for循环遍历列表
在for循环中将列表的元素添加至集合
最终得到元素去重后的集合对象，并打印输出
"""

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'best']
my_set = set()
for item in my_list:
    my_set.add(item)
print(my_set)