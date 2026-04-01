"""
演示地图可视化的基本使用

"""
from pyecharts.charts import Map

#准备地图对象
map = Map()

# 准备数据
data = [("北京", 99),("上海", 199),("湖南", 299),("台湾", 399),("广东", 499)]

# 添加数据
map.add("测试地图", data, "china")

# 绘图
map.render(path="./04_地图可视化.html")

# 设置全局选项