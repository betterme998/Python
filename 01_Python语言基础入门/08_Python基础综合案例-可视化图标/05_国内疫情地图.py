"""
演不全国疫持可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
json_data = None
with open("./疫情.txt", "r", encoding="utf-8") as f:
  json_data = f.read()
#将字符串json转换为python字典
data_dict = json.loads(json_data)
all_provinces = ['北京市', '天津市', '上海市', '重庆市','河北省', '山西省', '辽宁省', '吉林省', '黑龙江省','江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省','河南省', '湖北省', '湖南省', '广东省', '海南省','四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省','台湾省','内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区','香港特别行政区', '澳门特别行政区']

# 取到各省数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = [] #绘图需要的数据
for province_data in province_data_list:
  province_name = province_data["name"] #省份名称
  for city in all_provinces:
    if province_name in city:
      province_name = city
  
  province_confirm = province_data["total"]["confirm"]#确诊人数
  data_list.append((province_name, province_confirm))




# 创建地图对象

map = Map()

# 添加教据
map.add("各省份确诊人数",data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
  title_opts=TitleOpts(title="全国疫情地图"),
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
map.render("./05_国内疫情地图.html")