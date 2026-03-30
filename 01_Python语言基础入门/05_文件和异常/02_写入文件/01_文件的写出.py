"""
.2 写文件  
f.write('hello world')  
f.flush()

注意:  
直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区  
当调用flush的时候，内容会真正写入文件  
这样做是避免频繁的操作硬盘，导致效率下降(一堆，一次性写磁盘)
"""

# 打开文件，不存在的文件 r读 w写 a追加
f = open("./test.txt","w", encoding="UTF-8")# write号入
# write写入
f.write("hello world!!") #内容写入到内存中
# flush剧新
# f.flush() # 将内存中积攒的内容，写入到硬盘的文件中
# close关闭
f.close()  #内置了flush方法
# 打开一个存在的文件
# 如果文件已经存在会清空文件内容再写入 write写入、flush剧新
# close关闭