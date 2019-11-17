#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import json

field_list = ['field1', 'field2', 'field3']

rows = ['value1', 'value2', 'value3']

line = collections.OrderedDict()

index = 0
for i in range(len(rows)):
    line.update({field_list[index]: rows[i]})
    index += 1


for key, value in line.items():
    print key, ':', value
print line
print '-----------------'

# line = dict(line)

# for key, value in line.items():
#     print key, ':', value
line = json.dumps(line)
print type(line)
print line
print '-----------------'
line = json.loads(line)
print type(line)
print line


