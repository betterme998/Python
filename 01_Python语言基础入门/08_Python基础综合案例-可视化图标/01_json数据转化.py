"""
演示JS0N数据和Python字典的相互转换
"""
import json

# 准备列表，列表内每一个元素部是字典，将其转换为JSON
data = [{"name": "张三", "age":11}, {"name": "李四", "age":10}, {"name": "王五", "age":13}]

# 准备字典，将字典转换为JSON
json_str = json.dumps(data, ensure_ascii=False) #如果有中文，想正确展示的话需要设置ensure_ascii=False
print(json_str) #[{"name": "\u5f20\u4e09", "age": 11}, {"name": "\u674e\u56db", "age": 10}, {"name": "\u738b\u4e94", "age": 13}]
print(type(json_str))

# 将JSON字待串转换为Python数据类型[{k:V，k:v}，{k:V，k:v}]
s = '[{"name": "张三", "age": 11}, {"name": "李四", "age": 10}, {"name": "王五", "age": 13}]'
l = json.loads(s)
print(l)
print(type(l)) # <class 'list'>

# 将JSON字符申转换为Pythop数据类型{k:V，k:v}
s = '{"name": "张三", "age": 11}'
d = json.loads(s)
print(d)
print(type(d)) # <class 'dict'>  