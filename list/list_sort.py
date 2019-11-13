#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = []

for i in range(10):
    item = dict()
    item.update({'num': i+1})
    item.update({'child': []})
    data.append(item)

# def takeKey(elem):
#     return elem['num']

# data.sort(key=takeKey, reverse=True)
data.sort(key=lambda elem: elem['num'])

print data

