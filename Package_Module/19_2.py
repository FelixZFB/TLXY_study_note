# 5.2. OS-操作系统相关

# os模块
# os.getcwd()

import os

# 获取当前的工作目录
mydir = os.getcwd()
print(mydir)

# 改变当前的工作目录
# os.chdir('\Hello World\python_work')
# mydir = os.getcwd()
# print(mydir)

# 获取文件夹目录下的子文件夹及文件
ld = os.listdir()
print(ld)

# 递归创建文件夹
# 格式：os.makedirs(递归路径）
# 当前文件夹下创建一个haha文件夹
# rst = os.makedirs('haha')

# system() 运行系统shell命令
# 格式：os.system(系统命令）
rst = os.system('ls')
print(rst)

# getenv() 获取指定的系统环境变量值
# 格式： os.getenv('环境变量名‘）
rst = os.getenv('path')
print(rst)

# exit() 退出当前程序

# 值部分
print(os.pardir)
print(os.curdir)

# 当前系统的路径分隔符
print(os.sep)
print(os.linesep)

# 显示当前操作系统名称
print(os.name)

import sys
import platform

# 返回当前系统的平台标识
print(sys.platform)

# 获取操作系统版本号
print(platform.version() )

# abspath() 将路径转换为绝对路径
# relpath() 将路径转化为相对路径
# . 点号代表当前目录
# .. 双点号代表父目录

absp = os.path.abspath('..')
print(absp)
absp = os.path.abspath('.')
print(absp)

resp = os.path.relpath('.')
print(resp)

# 获取路径中的文件名
bn = os.path.basename('\Pcakage_Module')
print(bn)

# 检测目录文件是否存在
e = os.path.isdir('\Pcakage_Module')
print(e)



