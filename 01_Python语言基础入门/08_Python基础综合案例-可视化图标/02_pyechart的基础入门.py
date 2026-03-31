"""
演示pyecharts的基础入门
"""
# 导包
from pyecharts.charts import Line

# 创建一个折线图对象
Line = Line()

# 给折线图对象添加x轴的数据
Line.add_xaxis(["中国", "美国", "英国"])

# 给折线图对象添加y轴的数据
Line.add_yaxis("GDP", [30, 20, 10])

# 通过rander方法，将代码生成为图像
Line.render()

# 设置全局配置项
