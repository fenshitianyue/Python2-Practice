#!/usr/bin/env python
# -*- coding: utf-8 -*-

nums = [1, 2, 3, 4, 5]

# result = 1
# for num in nums:
#     result *= num
# print result

result = reduce(lambda x, y: x * y, nums)
print result

# 逆置字符串
s = 'hello world'
s = reduce(lambda x, y: y+x, s)
print s

