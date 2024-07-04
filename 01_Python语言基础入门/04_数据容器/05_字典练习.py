"""
⼈ 使⽤⼀个字典来存储⼀个⼈的信息，包括名、姓、年龄
和居住的城市。该字典应包含键 first_name、last_name、age 和
city。将存储在该字典中的每项信息都打印出来。
"""
value = {'frist_name': "张三", 'last_name': "李四", 'age': 18, 'city': "北京"}
print(value['frist_name'])
print(value['last_name'])
print(value['age'])
print(value['city'])

"""
--------------------------
"""

my_dict = {
  "王力宏": { "部门":"科技部", "工资":3000, "级别":1 },
  "张三": { "部门":"财务部", "工资":2000, "级别":1 },
  "李四": { "部门":"人事部", "工资":1000, "级别":2 },
  "王五": { "部门":"人事部", "工资":1000, "级别":2 },
  "赵六": { "部门":"人事部", "工资":1000, "级别":2 }
}
print(my_dict)
for item in my_dict:
  if my_dict[item]["级别"] == 1:
    my_dict[item]["级别"] += 1
    my_dict[item]["工资"] += 1000
print(my_dict)