#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = [
    {
        'attention_name': 'name1;name2;name3',
        'name': 'xxx事业群',
        'bg_id': 2,
        'children': [
            {
                'dept_id': 5,
                'name': 'xxx部门',
                'attention_name': 'name5;name4',
                'children': []
            },
            {
                'dept_id': 8,
                'name': 'xxx部门',
                'attention_name': 'name7;name8',
                'children': []
            }
        ]
    },
    {
        'attention_name': 'name9;name10;name31',
        'name': 'xxx事业群',
        'bg_id': 3,
        'children': [
            {
                'dept_id': 10,
                'name': 'xxx部门',
                'attention_name': 'name11;name12',
                'children': []
            },
            {
                'dept_id': 15,
                'name': 'xxx部门',
                'attention_name': 'name13;name15'
                # 'children': []
            }
        ]
    }
]


def get_item(raw_data, name):
    if raw_data is None:
        return None
    for it in raw_data:
        if name in it['attention_name']:
            return it
        else:
            return get_item(it.get('children'), name)
    # if raw_data is None or raw_data.get('attention_name') is None:
    #     return
    # if name in raw_data['attention_name']:
    #     return data
    # return get_item(raw_data.get('children'), name)

if __name__ == '__main__':
    # for it in data:
    item = get_item(data, 'name4')
    print item
