#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lambda关键字是用来创建内联函数的

"""

def square(x):
    return x * x
# ->
square_l = lambda x: x * x

print square(2)
print square_l(2)
