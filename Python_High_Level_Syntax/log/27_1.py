# 日志实例
#

import logging

# 设置输出格式
LOG_FORMAT = "%(asctime)s=====%(levelname)s+++++%(message)s"

# 设置输出的日志文件，设置输出什么级别的日志和日志的格式
# 该函数只在程序第一次调用时生效
logging.basicConfig(filename="27_1.log", level=logging.WARNING, format=LOG_FORMAT)

# 设置相应级别的日志
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
