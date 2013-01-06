#coding=utf-8
from StringIO import StringIO
from cStringIO import StringIO as cStrIO

'''
类似StringBuilder和StringReader, 使用str的list（self.buflist = []）实现
cStringIO效率更高, API相同

StringIO.write
StringIO.getvalue()    # ''.join(self.buflist)
StringIO.read()        # 每次read会join buflist，效率比较低
StringIO.readline()
'''

StringIO
cStrIO