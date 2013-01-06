#coding=utf-8
from textwrap import wrap, dedent

'''
对长字符串进行修整, 当一行长度超过指定字符数时截取
模块中含几个函数和TextWrapper类, 函数的作用是新建TextWrapper类并调用其方法
'''

s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# textwrap.wrap(text[, width[, ...]]) , width = 70
print wrap(s, 20)

# textwrap.dedent(text) , 移除所有行公共的前导空白
s = '''  
  aaa   
   bbb 
    ccc
'''
print dedent(s)