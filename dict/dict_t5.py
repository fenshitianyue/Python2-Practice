#!/usr/bin/env python
# -*- coding: utf-8 -*-

data_map = {
    'field1': []
}

if data_map.get('field1') is not None:
    print 'field1 had value'
else:
    print 'field1 not have value'

# if data_map.get('field2') is not None:
#     print 'field2 had value'
# else:
#     print 'field2 not have value'

if data_map.get('field1'):
    print 'field1 had value'
else:
    print 'field1 not have value'

