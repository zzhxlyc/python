#coding=utf-8
from copy import deepcopy

#-----------------copy---------------------
#slice[:] and list() are both copy, and it is shallow copy
l = ['name', [100, 'money']]
a = l[:]
b = list(l)
print id(l[0]), id(a[0]), id(b[0])  #same, shallow copy
print id(l[1]), id(a[1]), id(b[1])  #same, shallow copy

a[0] = 'stariy'
print l, a, b   #字符串是不可变类型
a[1][0] = 200
print l, a, b   #第二层的列表的指针被复制，第三层都一样


#-----------------deepcopy---------------------
'''
deepcopy会递归地复制对象中的可变类型（类、元组、列表、字典等）
不复制不可变类型（因为修改时重新创建新对象）（基本对象、字符串等）
'''
a = deepcopy(l)
b = deepcopy(l)
print id(l[0]), id(a[0]), id(b[0])  #all is same
print id(l[1]), id(a[1]), id(b[1])  #diff to each other, deep copy
print id(l[1][0]), id(a[1][0]), id(b[1][0]) #all is same

