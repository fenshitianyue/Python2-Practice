#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import time

def func():
    while True:
        # time.sleep(1)
        print 'coroutine run...'

if __name__ == '__main__':
    g1 = gevent.spawn(func)
    g1.join()
    print '---main func exit---'
    time.sleep(1)
