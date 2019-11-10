#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(filename='INFO.log',  # 要写入的日志文件名
                    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s : %(message)s',  # 写入的消息格式
                    level=logging.DEBUG  # 只有大于这里设置的消息级别的消息才可以被写入到日志文件中
                    )


logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.fatal('fatal')
logging.critical('critical')

