#coding=utf-8
from collections import deque

dq = deque()

dq.append(1)
dq.appendleft(2)

dq.reverse()

dq.pop()        #0元素IndexError
dq.popleft()    #0元素IndexError

if dq.count(1) > 0:
    dq.remove(1)    #不存在ValueError

dq.clear()

def __init__(self, iterable = None, maxlen = None):
    pass
    