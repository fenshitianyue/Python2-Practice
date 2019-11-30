#!/usr/bin/env python
# -*- coding: utf-8 -*-

file_in = 'zimu_in.txt'
file_out = 'zimu_out.txt'
data_list = []

def parse_func(filename):
    temp_data_list = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            temp_data_list.append(line.split('>')[1:])
            line = f.readline()
        for it in temp_data_list:
            if len(it) == 3:
                data_list.append(it[2])
            elif len(it) == 0:
                continue
            elif len(it) == 2 and (it[1].find('&nbsp') == -1 or it[1].find('\r\n') == -1):
                data_list.append(it[1])

def write_file(filename):
    with open(filename, 'w') as f:
        for line in data_list:
            f.write(line)


if __name__ == '__main__':
    parse_func(file_in)
    write_file(file_out)
