#coding=utf-8

'''
Create a memoryview that references obj. obj must support the buffer protocol. 
Builtin objects that support the buffer protocol include str and bytearray (but not unicode).
Readonly
'''

v = memoryview('abcefg')
data = bytearray('abcefg')

v.tolist()      #    [97, 98, 99, 101, 102, 103], a int list

