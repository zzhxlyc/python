#coding=utf-8
import re

'''
^     begin
$     end
\d    [0-9]        \D    [^0-9]
\s    [ \t\r\n]    \S    [^ \t\r\n]
\w    [a-zA-Z0-9]  \W    
\\    [\]
'''

#模式
re.I, re.IGNORECASE

pattern = '[\d]+'
num_re = re.compile(pattern)

#match, only match from beginning is ok, like a pattern with a ^(begin symbol)
if num_re.match('a123aasd'):
    print 'it is num'
    
#search, match from anywhere is ok
elif num_re.search('abc123'):
    print 'has num'
    
#match and search return a MatchObject, () is a place to get a value
matchObj = re.search('([\w]+)-([\w]+)', 'text-py')
if matchObj != None:
    print matchObj.group(0) #text.py
    print matchObj.groups() #('text', 'py')
    print matchObj.group(1), matchObj.group(2), matchObj.group(1, 2)  #text py ('text', 'py')
else:
    print None

#findall
matchList = num_re.findall('123abc456xyz789')
print matchList  #['123', '456', '789'], the result is a list

#replace, function sub(pattern, newStr, text)
str = 'stariy.info, i like info'
print re.sub('info', 'org', str)    #stariy.org, i like org
print re.sub('info', 'org', str, 1) #stariy.org, i like info
print re.subn('info', 'org', str)   #('stariy.org, i like org', 2)

#split    split(pattern, string[, maxsplit=0, flags=0]) 
print re.split('[a-f]+', '0a3B9', flags = re.I)

#escape 将所有非数字字母的字符加反斜杠
print re.escape('[hello] (world) {!} /')    #\[hello\]\ \(world\)\ \{\!\}\ \/


