#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_nth(source, target, num):
    start = source.find(target)
    while start >= 0 and num > 1:
        start = source.find(target, start+1)
        num -= 1
    return start


s = '10-11-12-'
t = '-'

print s[0:find_nth(s, t, 1)]
print s[find_nth(s, t, 1)+1:find_nth(s, t, 2)]
print s[find_nth(s, t, 2)+1:find_nth(s, t, 3)]
