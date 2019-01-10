# seek案例

# 打开文件后从第五个字节开始读取
with open('test01.txt', 'r') as f:
    f.seek(4, 0)
    strChar = f.read()
    print(strChar)

# 打开文件，每次读取3个字符
with open('test01.txt', 'r') as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        strChar = f.read(3)
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()





