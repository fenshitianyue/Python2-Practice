#!/usr/bin/env python
# -*- coding: utf-8 -*-

def square(x):
    return x * x

nums = [2, 4, 6, 8, 10]
nums_squared = [num * num for num in nums]
print type(nums_squared)
print nums_squared
print '-------------------'

nums_squared = map(square, nums)
print type(nums_squared)
print nums_squared
print '-------------------'

nums_squared = map(lambda x: x * x, nums)
print type(nums_squared)
print nums_squared
print '-------------------'

