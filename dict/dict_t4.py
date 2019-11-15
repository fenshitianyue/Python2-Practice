#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 这个函数中对data做的修改并没有影响到外部的data
def package(data):
    data = []
    data.append(4)
    data.append(5)


if __name__ == '__main__':
    data = [1, 2, 3]
    package(data)
    print data
