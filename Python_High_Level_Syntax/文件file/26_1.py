# coding: utf-8
# -*- coding: cp936 -*-

# **Python高级语法——文件实例

# 打开文件以写的方式
# r后面表示字符串内容不需要转义
# f称为文件句柄
# f = open(r'test01.txt', 'w')
# 这种文件打开的方式必须关闭
# f.close()


# with语句
# with open(r'test01.txt', 'r') as f:
    # pass
    # 接下来的代码开始对文件f进行操作
    # 本模块中不需要使用close关闭文件

# 写入文件
filename = 'test01.txt'

with open(filename, 'w') as f:
    f.write("I LOVE CODING.\n")
    f.write("I LOVE WORLD.\n")
    f.write("I LOVE EVERYONE.\n")

# 逐行读取
with open('test01.txt', 'r') as f:
    strline = f.readline()
    while strline:
        # rstrip删除行末尾的空格符
        print(strline.rstrip())
        strline = f.readline()

# 整个读取
with open('test01.txt', 'r') as f:
    strline = f.read()
    while strline:
        print(strline.rstrip())
        strline = f.read()

# 文件以列表返回
# 方法1
with open('test01.txt', 'r') as f:
    l = list(f)
    print(l)
    for line in l:
        print(line)

# 方法2 readlines逐行读取并存在一个列表中
with open('test01.txt', 'r') as f:
    l = f.readlines()
    print(l)
    for line in l:
        print(line)

# read直接读完，可以设定读取的字符个数
with open('test01.txt', 'r') as f:
    s = f.read()
    print(s)






