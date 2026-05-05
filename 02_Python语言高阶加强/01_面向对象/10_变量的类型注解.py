"""
演示变量的类型注解
一般，无法直接看出变量类型会添加变量的类型注解

帮助第三方IDE工具（如PyCharm）对代码进行类型推断，协助做代码提示  
帮助开发者自身对变量进行类型注释
"""

# 基础数据类型注解
# var_1: int = 10
# var_2: str = "hello"
# var_3: bool = True

#类对象类型注解
class Student:
  pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"num":666}
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "itheima", True)
my_dict: dict[str, int] = {"num":666}

# 在注释中进行类型注解
var_1 = random.randint(1, 10) # type: int
var_2 = json.loads('{"name": "张三"}') # type: dict[str, str]
def func():
  return 10
var_3 = func() # type: int

