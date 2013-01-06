import urlparse, urllib
# -*- coding: utf8 -*-

#parse URL
print '\nparse URL'
url = 'http://www.baidu.com/s?wd=python&from=a'
print urlparse.urlparse(url)
urlObj = urlparse.ParseResult(
    scheme='http', 
    netloc='www.baidu.com', 
    path='/s', 
    params='', 
    query='wd=python&from=a', 
    fragment=''
)
print urlparse.urlunparse(urlObj)

print urlparse.urlparse('www.baidu.com/s?wd=python')

#URl encode
print '\nURl encode'
url = 'http://blog.stariy.org/2010-12/北海 景山.html'
print urllib.quote(url)                     #change ' '(blank) to '%20', '/' is safe
print urllib.quote_plus(url)                #change ' '(blank) to '+',   '/' is unsafe
print urllib.quote_plus(url, '/')           #make '/' is safe char
print urllib.unquote(urllib.quote(url))     