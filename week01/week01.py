import logging
from datetime import datetime
import os

"""
编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：
/var/log/python- 当前日期 /xxxx.log
"""


def log_set(file_name):
    logging.basicConfig(filename=file_name,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s  %(name)s  %(levelname)-8s [line:%(lineno)d] %(message)s'
                        )


def mkdir(dir):
    if os.path.exists(dir):
        return

    else:
        os.makedirs(dir)


def test():
    logging.info("abc")
    logging.info("bab")
    logging.debug("hig")


if __name__ == '__main__':
    currentTime = datetime.strftime(datetime.now(), '%Y%m%d')
    path=f'/var/log/python-{currentTime}/week01.log'
    dir_name = os.path.dirname(path)
    mkdir(dir_name)
    log_set(path)
    test()
