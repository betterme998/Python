"""
(文件处理相关工具，内含:)
--函数:print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
--函数:append_to_file(file_name,data)，接收文件路径以及传入数据，将数据追加写入到文件中
"""

def print_file_info(file_name):
  try:
    with open(file_name, "r", encoding="utf-8") as f:
      print(f.read())
  except Exception as e:
    print("文件不存在")

def append_to_file(file_name,data):
  with open(file_name, "a", encoding="utf-8") as f:
    f.write(data)