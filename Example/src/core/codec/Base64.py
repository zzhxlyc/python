import base64

str = 'http://blog.stariy.org/2010-11/%e6%98%9f%e9%99%85%e4%ba%89%e9%9c%b8.html'

'''
base64 is good for string have much none ASC char

base64 has 64 char from A-Za-z0-9 and + and /, for normal
                        A-Za-z0-9 and - and _, for urlsafe
'''

print 'normal'
print base64.b64encode(str)         #aHR0cDovL2Jsb2cuc3Rhcml5Lm9yZy8=
print base64.b64decode(base64.b64encode(str))  #http://blog.stariy.org/

print '\nurlsafe'
print base64.urlsafe_b64encode(str)
print base64.urlsafe_b64decode(base64.urlsafe_b64encode(str))

print '\nstring'
#use for big string with '\n' and so on
print base64.encodestring(str)      #aHR0cDovL2Jsb2cuc3Rhcml5Lm9yZy8=, plus an extra '\n' as last
print base64.decodestring(base64.encodestring(str))         #http://blog.stariy.org/

