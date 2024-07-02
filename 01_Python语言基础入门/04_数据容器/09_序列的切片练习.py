"""
有字符串:"万过薪月，员序程马黑来，nohtyP学
请使用学过的任何方式，得到"黑马程序员"
"""
str = "万过薪月,员序程马黑来,nohtyP学"

#方法一
new_str = str[5:10]
print(new_str[::-1])

#方法二
str_list = str.split(',')
print(str_list[1][:5][::-1])