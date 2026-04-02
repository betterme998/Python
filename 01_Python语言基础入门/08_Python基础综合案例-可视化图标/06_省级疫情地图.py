"""
演示河南省疫悄地图开发

"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
json_data = None
with open("./疫情.txt", "r", encoding="utf-8") as f:
  json_data = f.read()

#json数据转换为python字典
data_dict = json.loads(json_data)

# 获取河南省数据#
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
#准备数据为元组并放入list
data_list = []
for city_data in cities_data:
  city_name = city_data["name"] + "市"
  city_confirm = city_data["total"]["confirm"]
  data_list.append((city_name, city_confirm))
print(data_list)

# 构建地图
map = Map()
map.add("河南省疫情地图", data_list, "河南")

# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
  title_opts=TitleOpts(title="省级疫情地图"),
  visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
      {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
      {"min": 100, "max": 999, "label": "100-999", "color": "#FFCCFF"},
      {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9999"},
      {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
      {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#FF9999"},
      {"min": 100000, "label": "100000+", "color": "#FF6666"},
    ]

  )
)
# 绘图
map.render("./06_省级疫情地图.html")