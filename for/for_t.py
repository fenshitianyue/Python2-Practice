#!/usr/bin/env python
# -*- coding: utf-8 -*-


data = []

for i in range(10):
    item = dict()
    item.update({'num': i+1})
    item.update({'child': []})
    data.append(item)

index = 5
for it in data:
    if it['num'] == 5:
        it['child'].append(4930)

print data

