# 7. 类的常用魔术函数

class A():
    def __init__(self):
        print("哈哈哈哈，我被调用了")

    def __call__(self):
        print("哈哈，我又被调用了一次")

    def __str__(self):
        return "哈哈，我又被调用了字符串函数"

# __init__ 就是一个魔法函数，自动调用
a = A()

# 实例当函数使用，自动调用__call__函数
a()

# 返回字符串函数
print(a)


# __str__ 和 __repr__的区别

class A():

    def __str__(self):
        return "__str__"

a = A()
print(a)

class A():

    def __repr__(self):
        return "__repr__"

a = A()
print(a)


# str和repr同时存在时候，返回字符串执行的是str函数
class A():

    def __str__(self):
        return "__str__"

    def __repr__(self):
        return "__repr__"

a = A()
print(a)

# str和repr本质区别，查看官方文档实例

import datetime

today = datetime.date.today()

# str返回的字符串可读性更强
print(str(today))

# repr返回结果应更准确。存在的目的在于调试，便于开发者使用。
# 细心的读者会发现将 __repr__ 返回的方式直接复制到命令行上，是可以直接执行的。
print(repr(today))



