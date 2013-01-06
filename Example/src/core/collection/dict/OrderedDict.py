#coding=utf-8
from collections import OrderedDict

'''
类似Java的LinkedHashMap, 使用链表保存插入顺序（更新key的时候不更新链表，与Java不同）
继承自dict, MutableMapping
self.__root = item = [ *PREV, *NEXT, key ] 
self.__map = {key : item}  保存链表节点，删除的时候用，省去遍历链表
'''

OrderedDict

def __setitem__(self, key, value, PREV=0, NEXT=1, dict_setitem=dict.__setitem__):
    if key not in self:
        root = self.__root
        last = root[PREV]   # 上一次插入最后的那个节点
        newItem = [last, root, key] #新项的节点, last指向上一个节点, root指向头结点
        last[NEXT] = root[PREV] =  newItem  #更新头结点的Prev和上一个节点的next