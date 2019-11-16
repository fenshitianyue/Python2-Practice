#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thread
import time

def func(thread_num):
    while True:
        time.sleep(1)
        print 'thread %d run...' % thread_num

thread.start_new_thread(func, (1,))
thread.start_new_thread(func, (2,))

while True:
    pass



