import xml.dom.minidom

'''
API doc 19.6 xml.dom
'''

xmlString = '<img src="a.jpg" alt="a.jpg" width="100" height="200">hello</img>'
parseObj = xml.dom.minidom.parseString(xmlString)
imgElement = parseObj.getElementsByTagName('img')[0]

print imgElement.nodeType == imgElement.ELEMENT_NODE, imgElement.tagName
print imgElement.hasAttribute('src'), imgElement.getAttribute('src')

print '\nText Node'
textNode = imgElement.childNodes[0]
print textNode.nodeType == textNode.TEXT_NODE, textNode.data

print '\nAttribute Node'
attrs = imgElement.attributes
i = 0
while i < attrs.length:
    attr = attrs.item(i)
    print attr.name, attr.value
    i += 1