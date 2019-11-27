#!/usr/bin/env python
# -*- coding: utf-8 -*-

# d = {
#     u'result': {
#         u'time_day': u'20190909',
#         u'doc_id': u'test doc_id'
#     }
# }
#
# result = d.get('result')
#
# print result

data = {
    'apm_entrance_name': 'test_name',
    'device': '91823-90182-12312',
    'version': '9.0.0.1',
    'os': None
}

get_field = lambda key: key if key is not None else 'enter else...'

print get_field(data.get('device'))
print get_field(data.get('os'))

