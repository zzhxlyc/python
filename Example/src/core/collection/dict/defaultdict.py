#coding=utf-8
from collections import defaultdict

'''
defaultdict构造有一个default_factory参数，指定value的类型, 在__missing__()中被使用
'''

def use_as_multi_dict():
    dd = defaultdict(list)
    L = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for key, value in L:
        dd[key].append(value)
    print dd.items()
    
def use_as_counter():
    dd = defaultdict(int)
    L = ['a', 'b', 'c', 'a']
    for key in L:
        dd[key] += 1
    print dd.items()

use_as_counter()