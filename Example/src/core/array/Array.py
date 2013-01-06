import array

'''
c            char
h            short            H            unsigned short
i            int              I            unsigned int
l            long             L            unsigned long
f            float            d            double
'''

intArray = array.array('i')
print 'itemsize'
print intArray.itemsize #4 bytes for a 32bit integer, but in list it is at least 12 bytes

intArray.append(1)
intArray.append(2)
intArray.append(3)

print '\nget'
print intArray[2]

#transfer with list
print '\ntransfer with list'
intList = intArray.tolist()
print intList
listArray = array.array('i')
listArray.fromlist(intList)
print listArray

#transfer with string
print '\ntransfer with string'
intString = intArray.tostring()
print intString
stringArray = array.array('i')
stringArray.fromstring(intString)
print stringArray

#transfer with file