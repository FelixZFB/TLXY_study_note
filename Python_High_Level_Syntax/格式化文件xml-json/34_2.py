import json

data = {"name": "Felix", "age": 20}

# 以写的方式打开，如果没有则新建一个
with open('34_2.json', 'w') as f:
    # 将data的内容写入到json文件中
    json.dump(data, f)

# 以读的方式打开文件
with open('34_2.json', 'r') as f:
    # 读取json文件中的内容保存在d中
    d = json.load(f)
    print(d)
