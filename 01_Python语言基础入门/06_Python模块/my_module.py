__all__ = ['test'] #当使用*号引入模块时，只能引入__all__中的内容

def test(a, b):
  print(a + b)

  #不想只是单纯引入就执行函数，可以通过判断__name__来决定是否执行
  if __name__ == '__main__': #__name__是python内置的变量，表示当前模块名
    test(1, 2) #当模块被直接运行时，__name__的值为__main__

def test_b(a, b):
  print(a - b)