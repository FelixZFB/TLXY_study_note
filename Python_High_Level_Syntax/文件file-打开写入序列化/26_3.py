# pickle序列化实例

import pickle

age = 19

with open('test02.txt', 'wb') as f:
    pickle.dump(age, f)

# 反序列化，读取文件
with open('test02.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)


# 序列化写入一个列表
a = [20, 'Felix', 'Zhang']

with open('test03.txt', 'wb') as f:
    pickle.dump(a, f)

# 反序列化，读取文件
with open('test03.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)


# 持久化shelve
# shv相当于一个字典
import shelve

shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 查看项目文件夹创建了三个shv文件，实际是个数据库

# 读取shelve案例
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['two'])
    print(shv['five'])
except Exception as e:
    print("没有这个元素")
finally:
    shv.close()
