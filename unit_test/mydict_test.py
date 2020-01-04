#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    """Dict 的单元测试类"""
    def test_init(self):
        d = Dict(number=1, string='test')
        self.assertEquals(d.number, 1)
        self.assertEquals(d.string, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            print "d['empty'] = {}".format(d['empty'])

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            print "d.empty = {}".format(d.empty)

    def setUp(self):
        """此函数在每一个测试用例调用之前执行"""
        print "set up..."
        # d = Dict()

    def tearDown(self):
        """此函数在每一个测试用例调用之后执行"""
        print "tear down..."


# 加上这两行代码，可以把测试用例作为普通的py脚本运行: python xx_test.py
# 否则，需要这样运行测试用例: python -m unittest xx_test
# if __name__ == '__main__':
#     unittest.main()

