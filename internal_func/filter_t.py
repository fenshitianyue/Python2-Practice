#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(n):
    return n % 2 == 1

nums = [1, 2, 3, 4, 5]

# odds = filter(func, nums)
odds = filter(lambda n: n % 2 == 1, nums)


print odds
