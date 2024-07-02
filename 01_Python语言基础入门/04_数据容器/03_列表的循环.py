"""
演示对list列表的循环，使用while种for循环2种方式
"""

def list_while_func():
    """
    使用while循环，对list列表进行循环
    :return:
    """
    # 定义一个list列表
    my_list = [1, 2, 3]
    # 使用while循环，对list列表进行循环
    index = 0
    while index < len(my_list):
        print("my_list[{}]: {}".format(index, my_list[index]))
        index += 1
list_while_func()

def list_for_func():
    """
    使用for循环，对list列表进行循环
    :return:
    """
    # 定义一个list列表
    my_list = [1, 2, 3]
    # 使用for循环，对list列表进行循环
    for item in my_list:
        print("item: {}".format(item))
list_for_func()