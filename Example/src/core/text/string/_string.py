#coding=utf-8
import string

'''
string是一个包含字符串处理的模块，有很多函数和常量，还有Formatter和Template类
'''

string.Formatter     # str.format()

'''
用$value的模板语法
'''
t = string.Template('$a = $b')
print t.substitute(a = 1, b = 2)
print t.safe_substitute({'a':3, 'b':4})     #KeyError exception
