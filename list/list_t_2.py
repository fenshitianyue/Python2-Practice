#!/usr/bin/env python
# -*- coding: utf-8 -*-

raw_data = [
    {
        'id': 1,
        'name': 'jack'
    },
    {
        'id': 2,
        'name': 'jack'
    },
    {
        'id': 3,
        'name': 'jack'
    },
    {
        'id': 4,
        'name': 'jack'
    },
    {
        'id': 5,
        'name': 'jack'
    }
]

filter_id = [1, 3, 5]

for it in raw_data:
    print it
    if it['id'] in filter_id:
        continue
    else:
        raw_data.remove(it)

print raw_data

def reset_list(l):
    del l[:]
    l = []
    l.append(100)

reset_list(filter_id)

print filter_id



