#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import timeit
import time

list_1 = ['短视频', '测试产品2', '测试产品3', '测试产品4']

####################################################
# 计时
# start = time.time()
def test_time_raw():
    count = 1000
    for i in range(count):
        list_1.append('测试产品x')
# end = time.time()

####################################################

# print '运行时间：', end - start
print timeit('test_time_raw()', 'from __main__ import test_time_raw', number=1000)



