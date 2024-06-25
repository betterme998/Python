
sum = 5000000
name =  input('请输入姓名:')

def atm_fun(name):
  print("---------------主菜单---------------")
  print(f"{name}，您好，请选择您的操作选项：")
  print('''
  查询余额\t[输入1]
  存款\t\t[输入2]
  取款\t\t[输入3]
  退出\t\t[输入4]
  ''')
  input_num = input("请输入操作选项:")
  return input_num


def atm_1(name):
  print("---------------查询余额---------------")
  print(f"{name}，您好，您的余额剩余：%d元" % sum)

def atm_2(name):
  print("---------------存款---------------")
  money = input(f"{name}，您好，请输入存款金额:")
  global sum
  sum += int(money)
  print(f"{name}，您好，您的余额剩余：%d元" % sum)
def atm_3(name):
  print("---------------取款---------------")
  money = input(f"{name}，您好，请输入取款金额:")
  global sum
  sum -= int(money)
  print(f"{name}，您好，您的余额剩余：%d元" % sum)
atm_fun(name)

while True:
  keyboard = atm_fun(name)
  if keyboard == '1':
    atm_1(name)
    continue
  elif keyboard == '2':
    atm_2(name)
    continue
  elif keyboard == '3':
    atm_3(name)
    continue
  else:
    break
