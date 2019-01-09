# collection模块
# namedtuple

import collections
# help(collections.namedtuple)
# 定义一个点
Point = collections.namedtuple("Point", ['x', 'y'])
p = Point(11, 12)
print(p.x)
print(p.y)
print(p[0])
print(p[1])

# 定义一个圆
Circle = collections.namedtuple("Circle",['x', 'y', 'r'])
c = Circle(100, 150, 50)
print(c)
print(c.x)
print(type(c))

# c是不是一个tuple(元组)
i = isinstance(c, tuple)
print(i)


# dequeue
from collections import deque

q = deque(['a', 'b', 'c'])
print(q)
q.append('d')
q.appendleft('x')
print(q)

# defaultdict

