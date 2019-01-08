# Python——包(Package)--模块(Module)实例

# 日历和时间模块

import sys

# 模块的搜索路径，获取19_1.py模块的路径列表
print(type(sys.path))
# print(sys.path)

for p in sys.path:
    print(p)


# 常用模块


# 日历模块
import calendar

# 三个参数
# help(calendar)
# w = 每个日期之间的间隔字符
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数

cal = calendar.calendar(2017, w=0, l=0, c=5)
print(type(cal))
# print(cal)

# isleap: 判断某一年是否闰年
print(calendar.isleap(2000))

# leapdays: 获取指定年份之间的闰年数
# help(calendar.leapdays)
print(calendar.leapdays(2000, 2018))

# monthcalendar() 返回一个月的矩阵列表
m = calendar.monthcalendar(2018, 3)
print(type(m))
print(m)

# 直接打印一年的日历
y = calendar.prcal(2018)

# prmonth 打印一个月的日历
calendar.prmonth(2018, 3)

# 时间模块
# time 时间戳
# 是从1970年1月1日0分0秒到现在经历的秒数
# 32位操作系统能够支持到2038年

import time

# 当前时区和UTC时间相差的秒数
print(time.timezone)

# 获取当前时区与UTC时间相差的秒数，在有夏令时的情况下
print(time.altzone)

# 测取当前是否为夏令时时间状态，0表示是
print(time.daylight)

# 获取时间戳
print(time.time())

# 获取时间元组，获取时间的结构
t = time.localtime()
print(type(t))
print(t)

# 获取时间结构的可读性强输出
tt = time.asctime(t)
print(type(tt))
print(tt)

# 获取时间戳，以浮点数表示
# 方法1
t = time.time()
# 浮点函数
print(float(t))
# 浮点函数，保留1位小数
print(round(t, 1))

# 方法2
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

print(time.process_time())

# sleep : 使程序进入睡眠，n秒后继续

for i in range(10):
    print(i)
    # time.sleep(1)

# strftime 将时间元组转化为自定义的字符串
# 把时间表示成2018年3月26日 21:05

t = time.localtime()
print(t)
print(time.strftime("%b %d %Y %H:%M:%S", t))

t = time.mktime(t)
print(t)

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print(time.strftime("%b %d %Y %H:%M:%S", t))

# datetime模块
# 提供日期时间属性的模块

import datetime
dt = datetime.date(2018, 3, 26)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)

# datetime.datetime

from datetime import  datetime, timedelta

dt = datetime.now()
print(dt)

# 格式化时间
print(dt.strftime("%Y-%m-%d %H:%M:%S"))


t1 = datetime.now()
# td表示以小时的时间长点
td = timedelta(hours=1)
# 当前时间加上一个小时后时间
t2 = t1 + td
print(t2.strftime("%Y-%m-%d %H:%M:%S"))


# timeit 时间测量工具

def p():
    time.sleep(5)

t1 = time.time()
# p()
t2 = time.time() - t1
print(t2)


# 生成列表需要的时间
import timeit

t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=10000)
print(t1)

# timeit 可以执行一个函数，来测量一个函数的执行时间

def doit():
    num = 3
    for i in range(num):
        return None

# 执行函数10次，重复10次所用的时间
t = timeit.timeit(stmt=doit, number=1000000)
print(t)













