#!/usr/bin/env python
# -*- coding: utf-8 -*-


list1 = ['field1', 'field2']

list2 = ['alias1', 'alias2']

for field, alias in zip(list1, list2):
    print ''.join([field, ' : ', alias])
