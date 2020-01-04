# -*- coding: utf-8 -*-

class Dict(dict):
    """Python dict 类的子类
    相比于dict原本的取值方式，还支持 object.key 的方式取值
    """
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict's object has no attribute: {}".format(key))

    def __setattr__(self, key, value):
        self[key] = value
