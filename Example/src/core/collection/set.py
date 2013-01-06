#coding=utf-8
'''
s = set(sequence)
fs = frozenset(sequence)
'''

s = set('abcde')    # 'abcde'是个char的序列，set中的元素是5个char
fs = frozenset(s)

s.add('a')
s.remove('a')       #若obj不在set中，抛ValueError
s.discard('a')      #若obj在set中则删除
s.clear()

s.issubset(fs)
s.issuperset(fs)

s.union(fs)
s.intersection(fs)
s.difference(fs)
