import time

# 获取时间戳，以浮点数表示
# 方法1
t1 = time.time()
filename1 = str(t1)
print(filename1)
time.sleep(1)
t2= time.time()
filename2 = str(t2)
print(filename2)
filename3 = str(t2) + '.jpg'
print(filename3)




