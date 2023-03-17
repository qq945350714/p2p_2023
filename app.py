# 日志初始化
import logging
import time
from logging import handlers
import os

base_url = "http://user-p2p-test.itheima.net/"
db_url = "121.43.169.97"
db_user = "student"
db_pwd = "P2P_student_2022"
db_name = "czbk_member"


# 获取当前py文件的绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))


def init_log():
    # 1.初始化日志对象
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3. 创建处理器
    sh = logging.StreamHandler()

    # 定义文件日志输出的文件路径和名字  os.sep是分隔符,会自动匹配Linux和Windows
    filename = base_dir + "log" + "os.sep" + "log.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='M', interval=3, backupCount=5, encoding='utf-8')

    # 4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)