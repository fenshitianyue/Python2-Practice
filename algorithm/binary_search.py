#!/usr/bin/env python
# -*- coding: utf-8 -*-


bg_data = []
for i in range(10):
    tmp = dict()
    tmp.update({'bg_id': i+1})
    tmp.update({"bg_name": "某某某事业群"})
    tmp.update({"humans": "human_a,human_b"})
    tmp.update({"children": []})
    bg_data.append(tmp)


def bin_search(data, target):
    start = 0
    end = len(data)
    while start <= end:
        mid = (start + end) // 2
        if data[mid]['bg_id'] == target:
            return mid
        elif data[mid]['bg_id'] < target:
            start = mid + 1
        else:
            end = mid - 1

tmp = {
    'dept_id': 2,
    'dept_name': '产品2',
    'humans': 'name1,name2',
    'children': []
}

index = bin_search(bg_data, tmp['dept_id'])
bg_data[index]['children'].append(tmp)

print bg_data[index]
print bg_data[index]['children']

