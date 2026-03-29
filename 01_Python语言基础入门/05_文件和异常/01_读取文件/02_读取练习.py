"""
通过windows的文本编辑器软件，将如下内容，复制并保存到:word.txt，文件可以存储在任意位置
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima
通过文件读取操作，读取此文件，统计itheima单词出现的次数
"""
sun = 0

with open("./word.txt","r", encoding="utf-8") as f:
  for line in f:
    sun += line.count("itheima")
  print(f"itheima单词出现了{sun}次")
