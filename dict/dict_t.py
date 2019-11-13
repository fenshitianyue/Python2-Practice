#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    "bg_id": 2,
    "bg_name": "某某某事业群",
    "humans": "human_a,human_b",
    "children": []
}

# print data
# print '----------------------'
#
# del data['humans']
# print data

name = 'human_a'

if name in data['humans']:
    print data['bg_id']
    print data['bg_name']
else:
    print 'not found'
