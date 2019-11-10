#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

reload(sys)
sys.setdefaultencoding('utf8')

# interface_url = 'http://127.0.0.1:8000/web/10000/singleCase/caseRecordCounts'
interface_url = 'https://www.baidu.com'
# param_list = {
#     'values': json.dumps({"zone": "lag_df", "p_id": 10000}),
#     'types': 'caton'
# }

def print_get_case_counts():
    # cookie = requests.cookies.RequestCookieJar()
    # cookie.set('token', 'something')
    # result = requests.get(interface_url, params=param_list, cookies=cookie, verify=False)
    result = requests.get(interface_url, verify=False)
    print result.url
    print result.content

if __name__ == '__main__':
    print_get_case_counts()
