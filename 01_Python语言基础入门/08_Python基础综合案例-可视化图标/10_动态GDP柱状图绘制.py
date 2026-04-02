"""
演示第三个图表:GDP动态桂状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

# 读取数据
data_lines = []
with open("./1960-2019全球GDP数据.csv","r",encoding="GB2312") as f:
  data_lines = f.readlines()
# 删除第一条数据
data_lines.pop(0)

# 将数据转换为字典存储，格式为:
# 年份:[[国家，gdp]，[国家,gdp]，......]，年份:[[国家，gdp]，[国家,gdp]，......
data_dict = {}
for line in data_lines:
  year = int(line.split(",")[0]) #年份
  country = line.split(",")[1] #国家
  gdp = float(line.split(",")[2]) #有科学计数法所以用float转一下
  #如何判断字典里面有没有指定的key？
  try:
    data_dict[year].append([country,gdp]) #如果没有报错说明有这个年份，就往里面添加数据
  except KeyError:
    data_dict[year] = [] # 报错了就创建一个年份
    data_dict[year].append([country,gdp])

#创建时间线对象
timeline = Timeline()

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
  data_dict[year].sort(key=lambda elememt: elememt[1], reverse=True)
  #取出本年份前8名的国家
  year_data = data_dict[year][0:8]
  x_data = []
  y_data = []
  for country_gdp in year_data:
    x_data.append(country_gdp[0])#x轴添加国家
    y_data.append(country_gdp[1]/100000000)#y轴添加gdp数据
  
  # 构建柱状图
  bar = Bar()
  x_data.reverse()
  y_data.reverse()

  bar.add_xaxis(x_data)
  bar.add_yaxis("GDP亿", y_data, label_opts=LabelOpts(position="right"))

  #反转x轴和y轴
  bar.reversal_axis()
  # 设置每一年的图标的标题
  bar.set_global_opts(
    title_opts=TitleOpts(title=f"{year}年全球前8GDP国家")
  )
  timeline.add(bar, str(year))

# 创建时间线对象
# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# #在for中，将每一年的bar对象添加到时间线中
# 自动播放设置
timeline.add_schema(
  play_interval=1000,# 播放间隔
  is_timeline_show=True,# 是否显示时间轴
  is_auto_play=True,# 是否自动播放
  is_loop_play=True,# 是否循环播放
)

# 绘制
timeline.render("./10_动态GDP柱状图绘制.html")