
# 装饰器
# 对hello函数进行扩展
# 高阶函数，以函数作为参数

import time


def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)

    return wrapper()


# 上面定义了一个装饰器。调用需要使用@
# hello函数就进行了扩展
@printTime
def hello():
    print("Hello world!")
hello

@printTime
def hello1():
    print("Hello world!")
hello1


# 偏函数
# 把字符串转化为十进制数字
l = int("12345")
# print(l)

# 求八进制的字符串12345，表示成十进制的数字是多少
l = int("12345", base=8)
# print(l)

# 新建一个函数，函数默认输入的是的字符串是16进制的数字
# 把此字符串转化成十进制和八进制的数字
def int16(x, base=16):
    return int(x, base)
print(int16("12345"))


def int10(x, base=16):
    return int(x, base=8)
print(int10("12345"))


# 偏函数
import functools
# 实现上面int16的功能
int16 = functools.partial(int, base=16)
print(int16("12345"))


# 高级函数补充
# zip实例
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]
l3 = zip(l1, l2)
print(type(l3))
print(l3)
for i in l3:
    print(i)

l1 = ['zhangfei', 'lisi', 'zhuergou']
l2 = [56, 76, 98]
l3 = zip(l1, l2)
for i in l3:
    print(i)

# enumerate实例
# 每个值添加一个索引
l1 = [1, 2, 3, 4, 5]
em = enumerate(l1)
l2 = [i for i in em]
print(l2)

em = enumerate(l1, start=100)
l2 = [i for i in em]
print(l2)