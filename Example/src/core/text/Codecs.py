#coding=utf-8
import codecs

'''
'''
encoding = 'utf-8'

#函数：(byte_str, char_size)
ef = codecs.getencoder('utf-8')     #<built-in function utf_8_encode>  
print ef('函数')      #('\xe5\x87\xbd\xe6\x95\xb0', 2)

# 函数： (Unicode_str, byte_size)
df = codecs.getdecoder('utf-8')
print df('函数')      #(u'\u51fd\u6570', 6)

reader = codecs.getreader(encoding)     #encodings.utf_8.StreamReader
print reader

writer = codecs.getwriter(encoding)
print writer

# codecs.open(filename, mode[, encoding[, errors[, buffering]]]) 
codecs.open('Re.py') 
