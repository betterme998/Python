my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {'name': 'Tom', 'age': 18}
my_set = {1, 2, 3}
my_str = 'hello'


# len元素个数
print(f"列表元素个数: {len(my_list)}")
print(f"元组元素个数: {len(my_tuple)}")
print(f"字典元素个数: {len(my_dict)}")
print(f"集合元素个数: {len(my_set)}")
print(f"字符串元素个数: {len(my_str)}")

# max最大元素
print(f"列表最大元素: {max(my_list)}")
print(f"元组最大元素: {max(my_tuple)}")
print(f"字典最大元素: {max(my_dict)}")
print(f"集合最大元素: {max(my_set)}")
print(f"字符串最大元素: {max(my_str)}")

# min最小元素
print(f"列表最小元素: {min(my_list)}")
print(f"元组最小元素: {min(my_tuple)}")
print(f"字典最小元素: {min(my_dict)}")
print(f"集合最小元素: {min(my_set)}")
print(f"字符串最小元素: {min(my_str)}")
 
# 类型转换：容器转列表list
print(f"元组转列表: {list(my_tuple)}")
print(f"字典转列表: {list(my_dict)}")
print(f"集合转列表: {list(my_set)}")
print(f"字符串转列表: {list(my_str)}")

# 类型转换：容器转元组tuple
print(f"列表转元组: {tuple(my_list)}")
print(f"字典转元组: {tuple(my_dict)}")
print(f"集合转元组: {tuple(my_set)}")
print(f"字符串转元组: {tuple(my_str)}")


# 类型转换：容器转字符串str
print(f"列表转字符串: {str(my_list)}") #"[1, 2, 3]"
print(f"元组转字符串: {str(my_tuple)}")#"('1', '2', '3')"
print(f"字典转字符串: {str(my_dict)}")
print(f"集合转字符串: {str(my_set)}")

# 类型转换：容器转集合set
print(f"列表转集合: {set(my_list)}")
print(f"元组转集合: {set(my_tuple)}")
print(f"字典转集合: {set(my_dict)}") #{"age", "name"}
print(f"字符串转集合: {set(my_str)}")

# sorted排序 返回list类型
print(f"列表排序: {sorted(my_list)}")
print(f"元组排序: {sorted(my_tuple)}")
print(f"字典排序: {sorted(my_dict)}")
print(f"集合排序: {sorted(my_set)}")
print(f"字符串CitCitCitCit排序: {sorted(my_str)}")

print(f"列表反向排序: {sorted(my_list, reverse=True)}")
print(f"元组反向排序: {sorted(my_tuple, reverse=True)}")
print(f"字典反向排序: {sorted(my_dict, reverse=True)}")
print(f"集合反向排序: {sorted(my_set, reverse=True)}")
print(f"字符串反向排序: {sorted(my_str, reverse=True)}")
