"""
演示地图可视化的基本使用

"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

#准备地图对象
map = Map()

# 准备数据
data = [("北京市", 99),("上海市", 199),("湖南省", 299),("台湾省", 399),("广东省", 499)]

# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
  visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
      {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
      {"min": 100, "max": 199, "label": "100-199", "color": "#FFCCFF"},
      {"min": 200, "max": 299, "label": "200-299", "color": "#FF9999"},
      {"min": 300, "max": 399, "label": "300-399", "color": "#FF6666"},
    ]
  )
)


# 绘图
map.render(path="./04_地图可视化.html")
