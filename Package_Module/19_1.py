# Python——包(Package)--模块(Module)实例

import sys

# 模块的搜索路径，获取19_1.py模块的路径列表
print(type(sys.path))
# print(sys.path)

for p in sys.path:
    print(p)


# 常用模块

import calendar
