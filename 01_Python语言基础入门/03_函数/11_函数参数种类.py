"""
函数参数种类
使用方式上的不同，函数有4中常见参数使用方式
.位置参数
.关键字参数
.缺省参数
.不定长参数
"""
def user_info(name, age, sex='男'):
    print('用户名：%s，年龄：%d，性别：%s' % (name, age, sex))

# 位置参数
user_info('张三', 18)

# 关键字参数
user_info(age=18, name='张三')

# 缺省参数(默认值) 必须写在最后面
user_info('张三', 18)

# 不定长参数
#1. 位置不定长参数
def user_info(name, age, *args):  # *args 接收所有位置参数,元组类型 (一般都用*args)命名
    print('用户名：%s，年龄：%d' % (name, age))
    for arg in args:
        print(arg)
user_info('张三', 18, '北京', '上海')
#2. 关键字不定长参数
def user_info(name, age, **kwargs): # **kwargs 接收所有关键字参数,字典类型 (一般都用**kwargs)命名
    print('用户名：%s，年龄：%d' % (name, age))
    for key in kwargs:
        print('%s:%s' % (key, kwargs[key]))
user_info('张三', 18, city='北京', province='上海')
