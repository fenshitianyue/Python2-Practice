#!/usr/bin/env python
# -*- coding: utf-8 -*-

parm = {'p_id': 10, 'message': 'hello world'}


print 'p_id: {p_id}, message: {message}.'.format(**parm)

print 'p_id: {}, message: {}.'.format(10, 'hello world')

print 'p_id: {1}, message: {0}.'.format('hello world', 10)
