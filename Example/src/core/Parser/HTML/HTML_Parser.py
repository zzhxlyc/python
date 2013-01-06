import htmllib, formatter

html = file('a.html','r')
data = html.read()
print data
html.close()

parser = htmllib.HTMLParser(formatter.NullFormatter())
#feed's param is the content to be parsed
str_to_be_parsed = '<img src="a.jpg" alt="a.jpg" width="100" height="200"/>'
str_to_be_parsed = '<a href="a.jpg" alt="a.jpg"/>'
parser.feed(str_to_be_parsed)
print parser.anchorlist

parser.close()