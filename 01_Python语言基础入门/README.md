# Python

Python 学习 1.初识 Python

2.什么是编程语言

3.Python 安装

4.Python 解析器
.Python 解释器，是一个计算机程序，用来翻译 Python 代码，并提交给计算机执行

5.Python 开发环境
.安装和配置 PyCharm 工具

# 常用的值类型

Python 中常用的有 6 种值类型：
.1.数字（number）
.整型（int）
.浮点型（float）
.布尔型（bool）：true 和 false 1 和 0
.复数（complex），如 4+3j，以 j 结尾表示复数

.2.字符串（string）

.3.列表（list）
.有序的可变的序列：Python 中使用最频繁的数据类型，可有效记录一堆数据

.4.元组（tuple）
.有序的不可变的序列：可有序记录一堆不可变的 python 数据

.5.字典（dictionary）
.无序 Key-Value 的集合：可无序记录一堆 Key-Value 型的 Python 数据

.6.集合（set）
.无序不重复集合：可记录一堆不重复的 Python 数据集合

# 注释的分类

.单行注释：# 注释内容
.多行注释：''' 注释内容 ''' 或 """ 注释内容 """ ：

# 变量

.在程序运行时，能存储计算机结果或能表示值的抽象概念：简单说，变量就是程序运行时，记录数据用的

# type() 函数

.type() 函数可以查看变量的类型

# print() 函数

print() 函数可以打印输出数据
print("aa",end=" ") # end 参数表示输出后不换行

print("hello\tworld")
print("hello\trld") # \t 输出一个制表符

\n 换行

# 输入函数 input()

input()函数让程序暂停运行，等待用户输入数据
.接收一个参数，表示输入提示信息

python 将用户输入的数据，以字符串的形式存储在变量中

# 数据类型转换

.常见的转换语句
.int()：将其他数据类型转换为 int 整型
.float()：将其他数据类型转换为 float 浮点型
.str()：将其他数据类型转换为 str 字符串

1.整数和浮点数
任意两个数相除，得到的结果都是浮点数，即便着两个数都是整数且结果为整数，结果也是浮点数.例子： 4/2 = 2.0

.在 python 中，只要有操作数中有一个浮点数，则结果都是浮点数，即便结果为整数，也是浮点数

2.数中的下划线
.书写很大数字的时候，可以使用下划线来分隔
age = 14_000_000
print(age) # 14000000

3.同时给多个变量赋值
x, y, z = 1, 2, "Tom"

4.常量
.常量：在程序运行过程中，值不能改变的量
.python 中没有内置的常量，但 python 程序员会使用大写字母指出某个变量视为常量
MAX_SPEED = 100

# 标识符

.标识符：在程序中，给变量、函数 类等起名字的符号

.标识符的命名规则：
.1.由字母、数字和下划线组成，不能以数字开头
.2.不能使用 Python 关键字作为标识符
.3.标识符不能包含空格
.4.标识符区分大小写，如 a 和 A 是两个不同的变量

# 变量命名规范

.1.见名知意，可读性强
.2.下划线命名法：
.3.英文字母全小写，单词间下划线连接

# 运算符

.算术运算符：+、-、\*、/、//（取整除）、%（取余数）、\*\*（幂）
.比较运算符：>、<、==（等于）、>=、<=、!=（不等于）
.复合赋值运算：=、+=、-=、\*=、/=、//=、%=

1.检查多个条件
.and：两个条件同时成立，结果才为真
.or：两个条件有一个成立，结果就为真
.not：取反，结果为真则为假，结果为假则为真
age1 = 20
age2 = 18
age1 >= 20 and age2 >= 20 # 两个条件同时成立，结果才为真
age1 >= 20 or age2 >= 20 # 两个条件有一个成立，结果就为真

2.检查特定值是否在列表中
.in：检查特定值是否在列表中，结果为真则为真，结果为假则为假
.not in：检查特定值是否在列表中，结果为真则为假，结果为假则为真
num = [1, 2, 3]
1 in num # 结果为真
4 not in num # 结果为真

# 字符串扩展

.一.字符串的三种定义方式
.1.单引号定义法：name = 'Tom'
.2.双引号定义法：name = "Tom"
.3.三引号定义法：name = '''Tom''' 或 name = """Tom"""
.三引号定义发：和多行注释写法一样，同样支持换行操作.使用变量接受它，它就是字符串，不使用变量接受它，就是多行注释

.二.字符串拼接
.三.字符串格式化输出
name = 'Tom'
message = 'Hello, %s' % name
print(message) # Hello, Tom

. % 表示我要占位
. s 表示将变成字符串放入占位的地方

.python 中最常用的三种类型占位
. %s 字符串占位符
. %d 整数占位符
. %f 浮点数占位符

.四.字符串的精度控制
.我们可以使用辅助符号 m.n 来控制字符串的精度
.m 操控宽度，要求是数字,设置的宽度小于数字自身，则不生效
.n 控制精度，要求是数字，小数点后的位数，会进行小数的四舍五入

示例：
.%5d 整数占位符，宽度为 5，如数字 11，则占位符为 00011，不足 5 位则补 0
.%5.2f 浮点数占位符，宽度为 5，小数点精度为 2，
小数和小数点也算入宽度计算如，数字 11.345 设置了%7.2f，则占位符为 011.35，不足 7 位则补 0，小数点后两位进行四舍五入为.35

.五.字符串格式化方式 2
不限数据类型，不做精度控制
通过语法：f"内容{变量}"的格式来快速格式化字符串
示例：
name = 'Tom'
year = 2019
price = 10.5
print(f'姓名：{name}，年龄：{year}，价格：{price}') # 姓名：Tom，年龄：2019，价格：10.5

.六.对表达式进行格式化
.1.了解什么是表达式
.表达式：一条具有运算结果的语句，如 1+2
print("1*1 的结果是: %d" % (1*1)) # 1\*1 的结果是: 1
print("字符串在 python 中的类型是: %s" % type("字符串")) # 字符串在 python 中的类型是: <class 'str'>

.六字符串的常用方法
.title()：将字符串的首字母大写
.upper()：将字符串中的所有字母全部大写
.lower()：将字符串中的所有字母全部小写

name = "tom"
name.title() # 将字符串的首字母大写
print(name.title()) # Tom

.七 制表符和换行符
.制表符：\t
.换行符：\n

.八 删除空白
.strip()：删除字符串左右两边的空白 不改变原字符串
.lstrip()：删除字符串左边的空白 不改变原字符串
.rstrip()：删除字符串右边的空白 不改变原字符串

.九 删除前缀
.removeprefix()：删除字符串前缀 不改变原字符串 # url = https://www.baidu.com url.removeprefix('https://') 得到 baidu.com
.十 删除后缀
.removesuffix()：删除字符串后缀 不改变原字符串 # url = https://www.baidu.com url.removesuffix('.com') 得到 https://www.baidu

# 数据输入

.数据输出：print()
.数据输入：input()
.使用 input()语句可以从键盘获取输入
.无论输入什么，input()都会将数据类型转换为字符串

# Python 判断语句

.布尔类型：True 和 False
.判断语句：if、elif、else # python 是以缩进来区分代码块的，4 个空格
.if 条件：
-- . 条件成立时，执行代码块

# 循环语句：while、for

for 循环用于针对集合中的每个元素执行代码块，而 while 循环则根据条件判断是否执行代码块

1.使用 while 循环处理列表和字典
.for 循环是一种遍历列表有效方式，但不应该在 for 循环中修改列表，否则会导致 python 难以跟踪其中的元素
.如果需要修改列表中的元素，则应该使用 while 循环

.while 条件:
-- . 条件成立时，执行代码块
.自行控制循环条件

.for 变量 in 列表:
.轮询机制，对一批内容进行 逐个处理 ：本质上是遍历：序列类型

.range() 函数：生成一个整数列表
.序列类型：指内容可以一个一个依次取出的一种类型，如列表、元组，字符串等
rang(num) 生成一个整数列表，从 0 到 num-1
rang(start,end) 生成一个整数列表，从 start 到 end-1
rang(start,end,step) 生成一个整数列表，从 start 到 end-1，步长为 step
rang(5,10,2) 取得的数据是:[5, 7, 9]

for 循环的变量作用域

.for 循环的变量，只在 for 循环中有效，出了 for 循环就无效了，实际上是可以访问到的，在编程规范书是不允许的

.for 循环的嵌套

.循环中断：break 和 continue
continue: 跳出本次循环，继续下一次循环 :可用于 for 循环和 while 循环
break: 跳出整个循环

# 函数

def 函数名(0 个或多个参数):
-- . 函数体
-- . return 返回值

特殊字面量:None
.表示：空，无意义
.用在 if 判断，None 等同于 False

1.函数的说明文档
def func(x,y):
"""
函数说明
:param x: 参数
:param y: 参数
:return: 返回值
"""
函数体
return x+y

2.函数的嵌套调用
.一个函数里调用另一个函数

3.函数作用域
.局部变量：函数内部定义的变量
.全局变量：函数外部定义的变量

.global 关键字
.在函数内部，使用 global 关键字声明全局变量

——————————————————————————————————————————————————
.1.实参和形参
greet_user(username) # username 是形参
greet_user('Tom') # 'Tom' 是实参

.2.传递实参
.位置实参：按照函数定义顺序，一一对应传递实参
.关键字实参：在调用函数时，按照 key=value 的形式传递实参

.位置实参
def pet(name, age):
print(f'我的宠物是 {name}，今年 {age} 岁了')
pet('小白', 1) # 我的宠物是 小白，今年 1 岁了

.关键字实参
def pet(name, age):
print(f'我的宠物是 {name}，今年 {age} 岁了')
pet(age=1, name='小白') # 我的宠物是 小白，今年 1 岁了

.3.默认值
def pet(name, age=2):
print(f'我的宠物是 {name}，今年 {age} 岁了')
pet('小白') # 我的宠物是 小白，今年 2 岁了

4.返回值
def sum(x, y):
return x + y

5.传递任意数量实参
.\*numbers 形参中的星号让 python 创建一个名为 numers 的空元组，并将传入的参数都打包到这个元组中

def sum(\*numbers):

6.结合使用位置实参和任意数量实参
def make_pizza(size,\*toppings):
print(f'我制作了一个 {size} 寸的披萨{toppings}')
make_pizza(16,'apple','banana') # 我制作了一个 16 寸的披萨('apple', 'banana')

7.使用任意数量的关键字实参
def build_profile(first, last, \*\*user_info):
user_info['first'] = first
user_info['last'] = last
return user_info
profile = build_profile('Tom', 'Smith', age=25, city='New York') # {'age': 25, 'city': 'New York'}S

形参\*\*user_info 形参中的双星号让 python 创建一个名为 user_info 的空字典，并将传入的参数都打包到这个字典中

8.将函数存储在模块中
pizza.py
.导入整个模块: import pizza
.导入模块中的函数: from pizza import make_pizza
.使用 as 关键字为函数指定别名: from pizza import make_pizza as mp
.使用 as 关键字为模块指定别名: import pizza as p
.导入模块中的所有函数: from pizza import \*

# 数据容器

python 中有 5 种数据容器：列表、元组、字典、集合、字符串
可以容纳多份数据类型，每一份数据称为元素，每个元素可以是任意类型

1.列表：[元素 1， 元素 2， 元素 3]
下标索引：从 0 开始，-1 表示最后一个元素
反向索引：从 -1 开始，-2 表示倒数第二个元素
最多容纳 2\*\*63-1 个元素

.列表的常用操作
.定义
.使用下标索引获取值
.插入元素
.删除元素
.清空列表
.修改元素
.统计元素个数

.1.查询下标 list.index(value)
.2.修改 list 元素 list[index] = value ：修改指定下标元素
.3.插入元素 list.inser(index, value) ：在指定位置插入元素
.4.追加元素 list.append(value) ：在列表末尾追加元素
.5.追加元素 list.extend(list) ：在列表末尾追加另一个列表
.6.删除元素 del list[index] ：删除指定下标元素
.7.删除元素 list.pop() ：删除列表末尾元素
.8.删除某元素 list.remove(value) ：删除列表中第一个 value 元素
.9.清空列表 list.clear() ：清空列表
.10.统计某个元素出现的次数 list.count(value)
.11.统计列表长度 len(list)

2.对数值列表执行简单的统计计算
.min() 获取列表中的最小值
.max() 获取列表中的最大值
.sum() 求列表中所有元素的和

3.列表推导式
squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
编写⼀⾏代码就能⽣成这样的列表

3.序列
序列指的是：内容连续，有序，可使用下标索引的一类数据容器
.列表，元组，字符串，均可以视为序列

.序列常用操作 - 切片
切片：从一个序列中，取出一个子序列

4.切片
.列表切片：list[start:end]
.start 默认值为 0，end 默认值为列表的长度
.负数表示从列表尾部开始计数

players = ['张三', '李四', '王五']
print(players[0:2]) # ['张三', '李四']
print(players[1:]) # ['李四', '王五']
print(players[:2]) # ['张三', '李四']
print(players[-1:]) # ['王五']
print(players[:-1]) # ['张三', '李四']

5.复制列表
包含整个列表的切片 [:] 复制整个列表
my_foods = ['苹果', '香蕉', '橘子']
friend_foods = my_foods[:]
print(my_foods) # ['苹果', '香蕉', '橘子']
print(friend_foods) # ['苹果', '香蕉', '橘子']

列表的遍历 -while 循环

6.元组
元组：不能修改元组中的元素
使用小括号 () 定义元组
my_foods = ('苹果', '香蕉', '橘子')
包含⼀个元素的元组，必须在这个元素后⾯加上逗号
my_t = (3,)

8.字符串
.方法：
.index 方法：返回指定字符串首次出现的索引
.replace 方法：替换字符串中的字符
.split 方法：将字符串拆分为列表
.strip 方法：去除字符串两边的空格
.count 方法：统计字符串中某个字符出现的次数
.len 方法：统计字符串的长度

.同元组一样，字符串是一个：无法修改的数据容器
.如果必须要做，得到的是一个新的字符串

.字符串特点
.只可以存储字符串
.长度任意（取决于内存大小）
.支持下标索引
.不可以修改（增加或删除元素等）
.支持循环

7.字典
字典(dictionary)是一系列键值对
.用{} 定义字典
aline = {'name': '阿莉', 'age': 18, 'gender': '女'}
print(aline['name']) # 阿莉

7.1 添加或修改字典元素
aline['age'] = 19
print(aline) # {'name': '阿莉', 'age': 19, 'gender': '女'}

7.2 删除字典元素
del 语句
del aline['age']
print(aline) # {'name': '阿莉', 'gender': '女'}

7.3 使用 get()方法获取字典元素
参数：get(key, default=None) 获取指定键的值，如果键不存在，则返回 default 的值

7.4 遍历字典
items() 方法: 返回字典中所有键值对列表
user = {'name': '阿莉', 'age': 18, 'gender': '女'}
for key, value in user.items():
print(key, value) # 依次打印字典的键值对

7.5 遍历字典的键
.keys() 方法: 返回字典中所有键列表
如果不使用 keys() 方法，for 循环遍历字典时，只能获取键，不能获取值
keys 可省略
user = {'name': '阿莉', 'age': 18, 'gender': '女'}
for key in user.keys():
print(key) # 依次打印字典的键，name age gender

7.6 按特定的顺序遍历字典的所有键
遍历字典时将按照键的插入顺序来遍历，如果想按照特定的顺序来遍历字典的键，可以使用 sorted() 方法
方案一.在 for 循环中对返回的键进行排序，可使用 sorted() 方法排序键列表

user = {'name': '阿莉', 'age': 18, 'gender': '女'}
for key in sorted(user.keys()):
print(key) # 依次打印字典的键，age gender name

7.6 遍历字典的值
values() 方法: 返回字典中所有值列表
user = {'name': '阿莉', 'age': 18, 'gender': '女'}
for value in user.values():
print(value) # 依次打印字典的值，阿莉 18 女

7.8 嵌套
.字典列表
alion01 = {'name': '阿莉', 'age': 18, 'gender': '女'}
alion02 = {'name': '阿莉', 'age': 18, 'gender': '女'}
users = [alion01, alion02]
for user in users:
print(user) # 依次打印字典列表中的字典，{'name': '阿莉', 'age': 18, 'gender': '女'} {'name': '阿莉',

.在字典中存储列表
user = {'name': '阿莉', 'age': 18, 'gender': '女'， 'hobbies': ['篮球', '足球']}

.在字典中存储字典
user = {'name': '阿莉', 'age': 18, 'gender': '女'， 'address': {'province': '广东', 'city': '深圳'}}

# 类

class Dog:
def **init**(self, name):
self.name = name

def bark(self):
print(f'{self.name}汪汪汪')
