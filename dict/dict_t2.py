#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 1


data = {}

# print data.get('ProductId')

for i in range(10):
    if i+1 in data.keys():
        data[i+1].append(10)
    else:
        data.update({i+1: []})
        data[i+1].append(10)

# print data

if num in data.keys():
    data[num].append(10)
else:
    data.update({num: []})
    data[num].append(10)

# print data

for key in data.keys():
    print key, ':', data[key]

