#!/usr/bin/env python
# -*- coding: utf-8 -*-

resp = [
    {
        'name': 'aiden',
        'id': 1,
    },
    {
        'name': 'aiden',
        'id': 1,
    },
    {
        'name': 'aiden',
        'id': 1,
    }
]

def del_attr(raw_data):
    for it in raw_data:
        del it['name']

print resp
del_attr(resp)
print resp
