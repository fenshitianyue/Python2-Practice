#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = ['field1', 'field2', 'field3']

index = 0

for element in l:
    print index, element
    index += 1

print '--------'

for i, element in enumerate(l):
    print i, element
