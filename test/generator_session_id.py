#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import time

session_id_dict = {}

def generator_session_id():
    # s1 = base64.encodestring(str(time.time()))
    # session_id_dict.update({'s1': s1 + ' -> ' + str(type(s1))})
    # s2 = base64.encodestring(str(time.time())).encode()
    # session_id_dict.update({'s2': s2 + ' -> ' + str(type(s2))})
    # s3 = base64.encodestring(str(time.time())).encode().decode()
    # session_id_dict.update({'s3': s3 + ' -> ' + str(type(s3))})
    # s4 = base64.encodestring(str(time.time())).encode().decode().replace('=', '')
    # session_id_dict.update({'s4': s4 + ' -> ' + str(type(s4))})
    # s5 = base64.encodestring(str(time.time())).encode().decode().replace('=', '')[::-2]
    # session_id_dict.update({'s5': s5 + ' -> ' + str(type(s5))})
    s6 = base64.encodestring(str(time.time())).encode().decode().replace('=', '')[::-2][::-1]
    session_id_dict.update({'s6': s6 + ' -> ' + str(type(s6))})
    s0 = base64.encodestring(str(time.time()))[::-1][3:]
    session_id_dict.update({'s0': s0 + ' -> ' + str(type(s0))})
    s7 = base64.urlsafe_b64encode(str(time.time()))
    session_id_dict.update({'s7': s7 + ' -> ' + str(type(s7))})


if __name__ == '__main__':
    generator_session_id()
    for key, value in session_id_dict.items():
        print key + ':' + value
        print '--------------------'
