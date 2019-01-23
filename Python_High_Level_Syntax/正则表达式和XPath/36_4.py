import re

title = '世界 你好，hello world'

# 匹配中文字符，找出所有的中文字符
p = re.compile(r'[\u4e00-\u9fa5]+')
rst = p.findall(title)

print(rst)




