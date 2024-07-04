# 定义字典
my_dict1 = {'name': 'Tom', 'age': 20}

# 定义空字典
my_dict1 = {}

# 定义重复key字典
my_dict1 = {'name': 'Tom', 'age': 20, 'name': 'Jerry'}
print(my_dict1)

# 从字典基于key获取value
my_dict1 = {'name': 'Tom', 'age': 20}
print(my_dict1['name'])

# 字典嵌套
my_dict1 = {'name': 'Tom', 'age': 20, 'address': {'province': 'Beijing', 'city': 'Shanghai'}}
print(my_dict1['address']['province'])

my_dict1 = {'name': 'Tom', 'age': 20}
# 新增元素
my_dict1['gender'] = 'male'
print(my_dict1)

# 更新元素
my_dict1['age'] = 21
print(my_dict1)

# 删除元素 
score = my_dict1.pop('age') # 删除元素并返回值
print(score)
print(my_dict1)

# 清空元素
my_dict1.clear()
print(my_dict1)

#获取全部key方法 keys()
my_dict1 = {'name': 'Tom', 'age': 20}
print(my_dict1.keys(), type(my_dict1.keys()))

# 遍历字典
# 方式一：获取全部key完成遍历
for key in my_dict1.keys():
    print(key,my_dict1[key])

# 方式二：直接for循环，每一次循环都是直接得到key
for key in my_dict1:
    print(key,my_dict1[key])

# 统计字典内元素数量
num = len(my_dict1)
print(num)

