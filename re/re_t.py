#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# def find_nth(source, target, num):
#     start = source.find(target)
#     while start >= 0 and num > 1:
#         start = source.find(target, start+1)
#         num -= 1
#     return start


attention_name = 'nels;tombie'

attention_name_2 = 'tombie;nels'

attention_name_3 = 'varoamfemh;nelsontang'

attention_name_4 = 'timenels;antfang'

attention_name_5 = 'fnelsion;tombie'

name = 'nels'

if __name__ == '__main__':
    pattern = '^{0};|;{1}$|;{2};'.format(name, name, name)
    print pattern
    result = re.search(pattern, attention_name_5)
    if result is not None:
        print result.span(0)
    else:
        print result




