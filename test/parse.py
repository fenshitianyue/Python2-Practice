#!/usr/bin/env python
# -*- coding: utf-8 -*-

file_in = 'zimu_in.txt'
file_out = 'zimu_out.txt'
data_list = []

def parse_func(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            line = ''.join(line.split('|')[1:])
            if line.find('&nbsp;') != -1:
                continue
            data_list.append(line)
            line = f.readline()

def write_file(filename):
    with open(filename, 'w') as f:
        for line in data_list:
            f.write(line)


if __name__ == '__main__':
    parse_func(file_in)
    # print data_list
    write_file(file_out)
