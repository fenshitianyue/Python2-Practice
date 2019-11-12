#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 想要知道字符串pos中是否包含指定的字符串有两种方法：

s = '__sum'
pos = 'field__sum'

# method 1
if s in pos:
    print 'True'
else:
    print 'False'

# medhod 2

if pos.find(s) != -1:
    print 'True'
else:
    print 'False'


