import xml.sax

'''
API doc 19.9 xml.sax
'''

xmlString = '<img src="a.jpg" alt="a.jpg" width="100" height="200">hello</img>'
parseObj = xml.sax.parseString(xmlString, xml.sax.handler.ContentHandler())
