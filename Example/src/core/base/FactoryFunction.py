import types

#int(), convert the string to int
print int('5'), 
print int('100', base = 16),  #Dec 256, The 100 is based on Hex, and the result is Dec
print int('111', 2) #Dec 7

#long() is same as int()
print long('100')

print float('3.5')

#complex()
print complex(3, 5)

#show the param's type
print 'type()',
print type(0), type(0 + 0j), type(''), type(None), type(()), type([]), type({}), type(type(0))
print dir(types)