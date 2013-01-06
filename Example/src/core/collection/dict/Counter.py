#coding=utf-8
from collections import Counter
from operator import itemgetter
import heapq

'''
继承自dict
'''

#支持任何序列
def update(self, iterable=None, **kwds):
    #将iterable和kwds中的元素添加到dict中，并更新计数
    pass

# nlogn
def most_common(self, n=None):
    if n is None:
        return sorted(self.iteritems(), key=itemgetter(1), reverse=True)
    return heapq.nlargest(n, self.iteritems(), key=itemgetter(1))

# 遍历时，重复元素的key将重复出现
def elements():
    c = Counter('CBAA')
    for char in c.elements():   #A A C B
        print char, 
