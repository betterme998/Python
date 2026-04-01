"""
演示可视化需求1 :折线图开发

"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts,VisualMapOpts, LabelOpts

text_url = ["./美国.txt","./日本.txt","./印度.txt"]
def data_hook(src):
  # 处理数据
  with open(src,"r", encoding="utf-8") as f_us:
    us_data = f_us.read()
    # 去掉不合JSON规范的开头,去掉不合JSON规范的结尾
    us_data = us_data[us_data.index("{") : -2]

    # # JSON转Python字典
    us_dict = json.loads(us_data)

    # # 获取trend key
    us_trand_data = us_dict["data"][0]['trend']

    # # 获取日期数据、用于x轴，取2020年(到314下标结束)
    us_x_data = us_trand_data['updateDate'][:314]

    # 获取确认数据，用于y轴，取2020年(到314下标结束)
    us_y_data = us_trand_data['list'][0]['data'][:314]
    return us_x_data,us_y_data

# 创建一个折线图对象
line = Line()
x_data_final = True
for s in text_url:
  x_data,y_data = data_hook(s)
  if x_data_final:
    # 给折线图对象添加x轴的数据
    line.add_xaxis(x_data)
    x_data_final = False
  # 给折线图对象添加y轴的数据
  line.add_yaxis(s[2:4], y_data, label_opts=LabelOpts(is_show=False))

# 设置全局配置项
line.set_global_opts(
  title_opts=TitleOpts(title="GDP展示"),# 标题
  legend_opts=LegendOpts(is_show=True), # 显示图例
  toolbox_opts=ToolboxOpts(is_show=True), # 显示工具箱
  visualmap_opts=VisualMapOpts(is_show=True), # 显示视觉映射
)
# 通过rander方法，将代码生成为图像
line.render(path="./03_折线图开发.html")
