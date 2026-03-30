"""
演示文件的追加写入
1.追加写入文件使用open函数的”a”模式进行写入
2.追加写入的方法有(和w模式一致):
wirte()，写入内容
flush()，刷新内容到硬盘中
3.注意事项:
a模式，文件不存在，会创建新文件
a模式，文件存在，会在原有内容后面继续写入
可以使用”\n”来写出换行符

"""

#打开文件，不存在的文件
f = open("./test.txt", "a",encoding="utf-8")
# write写入
f.write("追加写入")
#flush剧新
f.flush()
#close关闭
f.close()
#打开一个存在的文件#
# write写入、flush剧新
# close关闭