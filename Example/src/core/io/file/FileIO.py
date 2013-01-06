#coding=utf-8
'''
access_mode : r(read) w(write, from begin) +(rw) a(append) b(binary_mode)
'''

_file = file('StandardIO.log', 'r');
'''
iter(_file)         # for line in file:
_file.next()
'''

file.closed
file.encoding
file.mode
file.name
file.newlines

_file.read()        # read([size]), size of bytes
_file.readline()    # readline([size])
_file.seek(10)
_file.tell()        # the position

_file = file('StandardIO.log', 'w');
_file.truncate()    # truncate([size]), 无size用当前位置, 剪裁/扩大 文件
_file.write('abc')
_file.writelines(['a', 'b', 'c'])    # writelines(sequence)

def read():
    try:
        fileName = 'StandardIO.log'
    #    fileName = 'noSuchFile.log'
        logFile = file(fileName,'r')
        for eachLine in logFile: #the eachLine contain the \n itself already
            print eachLine, 
        logFile.close()
    except IOError, e:
        print 'file open error :', e

def write():
    try:
        fileName = 'BOM.txt'
        f = file(fileName,'w')
        #UTF-8 BOM, write bytes
        f.write('\xEF');f.write('\xBB');f.write('\xBF')
        f.close()
    except IOError, e:
        print 'file open error :', e  