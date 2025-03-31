"""
@author: 薯条老师
@desc:
"""

import logging
from configure import settings

import logging

# 配置日志信息
logging.basicConfig(level=settings.LOGGING_LEVEL,
                    format='%(asctime)s--%(levelname)--8s:%(message)s',
                    filename=settings.LOGGING_FILE,
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(settings.LOGGING_LEVEL)

formatter = logging.Formatter('%(asctime)s--%(levelname)--8s:%(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__file__)




