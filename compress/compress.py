#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip

with open('data.txt', 'r') as fr:
    content = fr.read()
    with gzip.open('pos.txt.gz', 'wb') as fw:
        fw.write(content)

