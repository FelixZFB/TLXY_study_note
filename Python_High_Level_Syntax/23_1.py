# Python高级语法——函数式编程

# '小'函数举例
def printA():
    print("AAAAA")


printA()

# lambda表达式(匿名函数)
# 以lambda开头
# 紧跟一定的参数，如果有的话
# 参数后用冒号和表达式主题隔开
# 只是一个表达式，所以没有return

# 计算一个数字的100倍
stm = lambda x: 100 * x
# 使用上跟调用函数一模一样
print(stm(100))

# 下式也可以定义为一个函数，返回一个值，但是表达式会比这个复杂的多
stm1 = lambda x, y, z: x + y * 10 + z * 100
print(stm1(4, 5, 6))


# 高阶函数，函数作为参数使用的函数
# 函数名称就是一个变量
def funA():
    print("In funA")


funB = funA
funA()
funB()


# 高阶函数举例
# funA是普通函数，返回一个传入数字的100倍的数字
def funA(n):
    return n * 100


# 在写一个普通函数，把传入的函数乘以300倍
def funB(n):
    return funA(n) * 3


print(funB(9))


# 写一个高阶函数，f = funA
def funC(n, f):
    # 假定函数是把n扩大100倍
    return f(n) * 3


print(funC(9, funA))


# 比较funC和funB,显热funC更灵活
# 例如n现在要放大30倍
# 如果要调用funB,需要修改funB的函数本体
def funD(n):
    return n * 10


print(funC(9, funD))

# map映射实例
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

# map实现上述功能
l1 = [i for i in range(10)]


def mulTen(n):
    return n * 10


l3 = map(mulTen, l1)
for i in l3:
    print(i)
print(l3)

# reduce实例
from functools import reduce


def myAdd(x, y):
    return x + y


# 对于列表[1, 2, 3, ....]执行,前一个加一个一直结束返回一个值
# 1到100的数字相加
rst = reduce(myAdd, [i for i in range(101)])
print(rst)


# filter函数
# 定义过滤函数
# 过滤函数要求有输入，返回布尔值
def isEven(a):
    return a % 2 == 0


l = [3, 3, 3, 45, 23, 54, 63, 24, 67, 5, 5, 6, 9, 8, 8]
rst = filter(isEven, l)
print(type(rst))
print(rst)
# 返回的就是filter数据，数据都进行了包装
# 采用for循环提取数据
print([i for i in rst])

# 排序案例
l = [3, 45, -7, 23, 54, -43, -78, 63, 24, 67, -120, 5, 6, 9, 8]
# 正序
al = sorted(l)
print(al)
# 倒序
al = sorted(l, reverse=True)
print(al)

# 按照绝对值排序
al = sorted(l, key=abs, reverse=True)
print(al)

# sorted案例
astr = ['abc', 'Tian', 'hafj', 'Xixi']
str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.lower)
print(str2)


# 函数作为值返回
def myF2():
    def myF3():
        print("In myF3")
        return 3

    return myF3


f3 = myF2()
print(type(f3))
print(f3)




